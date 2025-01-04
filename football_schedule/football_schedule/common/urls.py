from django.urls import path
from football_schedule.common.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
]