from django.urls import path

from football_schedule.schedules.views import ScheduleCreateView, ScheduleDisplayView

urlpatterns = [
    path('',ScheduleCreateView.as_view(),name='schedule'),
    path('display',ScheduleDisplayView.as_view(),name='schedule'),
]