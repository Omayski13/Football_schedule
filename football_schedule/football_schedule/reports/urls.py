from django.urls import path, include

from football_schedule.reports.views import ReportCreateView, processing_view, job_status, download_report, \
    InstructionsView

urlpatterns = [
    path('create/', ReportCreateView.as_view(), name='create-report'),
    path("processing/<uuid:job_id>/", processing_view, name="report-processing"),
    path("status/<uuid:job_id>/", job_status, name="job-status"),
    path("download/<uuid:job_id>/", download_report, name="report-download"),
    path("instructions/", InstructionsView.as_view(), name="instructions"),

]
