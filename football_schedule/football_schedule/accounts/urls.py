from django.contrib.auth.views import LogoutView
from django.urls import path, include

from football_schedule.accounts.views import UserRegisterView, UserLoginView, UserDetailsView, UserEditView

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name='user-logout'),
    path('profile/<int:pk>/',include([
        path('details/',UserDetailsView.as_view(), name='details'),
        path('edit/',UserEditView.as_view(), name='edit')
    ]))
]