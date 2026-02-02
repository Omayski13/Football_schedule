import os
import shutil
import tempfile
import zipfile

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404

from football_schedule.common.views import process_xlsm

import threading
import uuid

JOB_STATUS = {}

def run_job(job_id, input_path, output_dir):
    try:
        process_xlsm(input_path, output_dir)

        zip_path = os.path.join(output_dir, "results.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(output_dir):
                for file in files:
                    if not file.endswith(".zip"):
                        zipf.write(os.path.join(root, file), arcname=file)

        JOB_STATUS[job_id]["status"] = "done"
        JOB_STATUS[job_id]["zip_path"] = zip_path

    except Exception as e:
        JOB_STATUS[job_id]["status"] = "error"
        print("JOB ERROR:", e)


class ReportCreateView(LoginRequiredMixin, View):
    template_name = "reports/create-report.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        uploaded_file = request.FILES.get("file")
        if not uploaded_file:
            return render(request, self.template_name, {
                "error": "Upload a file"
            })

        job_id = str(uuid.uuid4())
        temp_input_dir = tempfile.mkdtemp()
        temp_output_dir = tempfile.mkdtemp()

        input_path = os.path.join(temp_input_dir, uploaded_file.name)
        with open(input_path, "wb+") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        JOB_STATUS[job_id] = {
            "status": "pending",
            "zip_path": None
        }

        threading.Thread(
            target=run_job,
            args=(job_id, input_path, temp_output_dir),
            daemon=True
        ).start()

        return redirect("report-processing", job_id=job_id)

def processing_view(request, job_id):
    return render(request, "reports/processing.html", {"job_id": job_id})


def job_status(request, job_id):
    job = JOB_STATUS.get(str(job_id))
    if not job:
        return JsonResponse({"status": "error"})

    return JsonResponse({"status": job["status"]})

def download_report(request, job_id):
    job = JOB_STATUS.get(str(job_id))
    if not job or job["status"] != "done":
        raise Http404

    return FileResponse(
        open(job["zip_path"], "rb"),
        as_attachment=True,
        filename="results.zip"
    )