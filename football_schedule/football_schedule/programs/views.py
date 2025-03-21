from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView

from football_schedule.programs.forms import MatchCreateForm, MatchEditForm
from football_schedule.programs.models import Match


# Create your views here.


class CreateMatchView(LoginRequiredMixin,CreateView):
    template_name = 'programs/create-program.html'
    form_class = MatchCreateForm
    success_url = reverse_lazy('create-program')

    def form_valid(self, form):

        match = form.save(commit=False)
        match.author = self.request.user

        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['matches'] = Match.objects.filter(author=self.request.user).order_by('date','time')

        return context

class EditMatchView(LoginRequiredMixin,UpdateView):
    template_name = 'programs/edit-match.html'
    form_class = MatchEditForm
    model = Match
    success_url = reverse_lazy('create-program')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user != self.object.author:
            if not self.request.user.is_superuser:
                raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

class DeleteAllMatchesView(View):
    def post(self, request, *args, **kwargs):
        # Delete all weeks created by the logged-in user
        matches_deleted, _ = Match.objects.filter(author=request.user).delete()
        messages.success(request, f"Successfully deleted {matches_deleted} matches.")
        return redirect('create-program')

def delete_match(request, pk):
    match = get_object_or_404(Match, pk=pk, author=request.user)
    match.delete()
    return redirect('create-program')

class DisplayProgramView(ListView):
    template_name = 'programs/display-program.html'
    model = Match


    def get_queryset(self):

        queryset = Match.objects.filter(author=self.request.user).order_by('date','time')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        dates = []
        matches = Match.objects.filter(author=self.request.user).order_by('date','time')
        for match in matches:
            if match.date not in dates:
                dates.append(match.date)

        context['dates'] = dates



        return context

