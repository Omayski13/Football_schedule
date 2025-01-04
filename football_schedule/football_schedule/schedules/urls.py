from django.urls import path, include

from football_schedule.schedules.views import ScheduleCreateView, ScheduleDisplayView, ScheduleWeekEditView, \
    DeleteAllWeeksView, delete_week

urlpatterns = [
    path('',ScheduleCreateView.as_view(),name='create-schedule'),
    path('display/',ScheduleDisplayView.as_view(),name='display-schedule'),
    path('delete-all-weeks/', DeleteAllWeeksView.as_view(), name='delete-all-weeks'),
    path('week/<int:pk>/',include([
        path('edit/',ScheduleWeekEditView.as_view(),name='edit-week'),
        path('delete/',delete_week,name='delete-week')
    ])),

]