from django.contrib.auth.views import LogoutView
from django.urls import path, include

from football_schedule.accounts.views import UserRegisterView, UserLoginView, UserDetailsView, UserEditView, \
    UserChangePasswordView, UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetView, \
    UserPasswordResetCompleteView

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(),name='user-logout'),
    path('profile/<int:pk>/',include([
        path('details/',UserDetailsView.as_view(), name='details'),
        path('edit/',UserEditView.as_view(), name='edit')
    ])),
    path('password/', include([
        path('change/', UserChangePasswordView.as_view(), name='change-password'),
        path('reset/', include([
            path('', UserPasswordResetView.as_view(), name='password-reset'),
            path('done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
            path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
            path('complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
        ])),
    ])),
]