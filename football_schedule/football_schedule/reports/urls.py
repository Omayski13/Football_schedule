from django.urls import path, include

from football_schedule.reports.views import ReportCreateView

urlpatterns = [
    path('create/',ReportCreateView.as_view(),name='create-report'),

    ]