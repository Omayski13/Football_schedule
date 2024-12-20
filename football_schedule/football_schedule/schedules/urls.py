from django.urls import path, include

from football_schedule.schedules.views import ScheduleCreateView, ScheduleDisplayView

urlpatterns = [
    path('',ScheduleCreateView.as_view(),name='create-schedule'),
    path('schedule/', include([
        path('',ScheduleDisplayView.as_view(),name='display-schedule'),
        # path('<int:pk>',name='edit-schedule'),
    ])),

]