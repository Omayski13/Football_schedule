from django.urls import path, include

from football_schedule.programs.views import CreateMatchView, DeleteAllMatchesView, delete_match, EditMatchView, \
    DisplayProgramView

urlpatterns = [
    path('create/', CreateMatchView.as_view(), name='create-program'),
    path('display/', DisplayProgramView.as_view(), name='display-program'),
    path('delete-all-matches/', DeleteAllMatchesView.as_view(), name='delete-all-matches'),
    path('match/<int:pk>/',include([
        path('delete/', delete_match, name='delete-match'),
        path('edit/', EditMatchView.as_view(), name='edit-match')
    ])),

]