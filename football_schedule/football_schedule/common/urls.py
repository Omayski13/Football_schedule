from django.urls import path
from football_schedule.common.views import HomeView, download_schedule_excel

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('download_excel/', download_schedule_excel, name='download_excel'),
]