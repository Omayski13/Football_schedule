import os
import shutil
import tempfile
import zipfile

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.templatetags.static import static

from football_schedule.common.views import process_xlsm


class ReportCreateView(LoginRequiredMixin,View):
    template_name = "reports/create-report.html"
    success_url = reverse_lazy('create-report')

    def get(self, request, *args, **kwargs):
        context = {
            'template_absence_file': static('files/template.xlsm')
        }
        return render(request, self.template_name, context)



    def post(self, request):
        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return render(
                request,
                self.template_name,
                {"error": "Please upload an XLSM file."}
            )

        # 1️⃣ Create temp dirs
        temp_input_dir = tempfile.mkdtemp()
        temp_output_dir = tempfile.mkdtemp()

        input_path = os.path.join(temp_input_dir, uploaded_file.name)

        # 2️⃣ Save uploaded file
        with open(input_path, "wb+") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # 3️⃣ Run your processing logic
        process_xlsm(input_path, temp_output_dir)

        # 4️⃣ Create ZIP
        zip_path = os.path.join(temp_output_dir, "results.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(temp_output_dir):
                for file in files:
                    if file.endswith(".zip"):
                        continue
                    full_path = os.path.join(root, file)
                    zipf.write(full_path, arcname=file)

        # 5️⃣ Return ZIP as download
        # with open(zip_path, "rb") as f:
        #     response = HttpResponse(
        #         f.read(),
        #         content_type="application/zip"
        #     )
        #     response["Content-Disposition"] = (
        #         'attachment; filename="results.zip"'
        #     )
        #     return response

        response = FileResponse(
            open(zip_path, "rb"),
            as_attachment=True,
            filename="results.zip",
            content_type="application/zip"
        )

        shutil.rmtree(temp_input_dir, ignore_errors=True)
        shutil.rmtree(temp_output_dir, ignore_errors=True)

        return response

