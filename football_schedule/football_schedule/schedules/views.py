from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView

from football_schedule.schedules.forms import WeekForm
from football_schedule.schedules.models import Week


# Create your views here.


class ScheduleCreateView(CreateView):
    template_name = 'schedules/create-schedule.html'
    form_class = WeekForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        week = form.save(commit=False)
        week.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['weeks'] = Week.objects.filter(author=self.request.user)

        return context




    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Handle AJAX DELETE request
        Week.objects.filter(author=request.user).delete()
        return JsonResponse({"message": "Weeks deleted successfully"})


class ScheduleDisplayView(ListView):
    template_name = 'schedules/display.html'
    context_object_name = 'weeks'

    def get_queryset(self):
        return Week.objects.filter(author=self.request.user)





