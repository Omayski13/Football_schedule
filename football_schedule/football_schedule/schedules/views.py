from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, UpdateView
from football_schedule.common.mixins import DeleteCloudinaryFormValidMixin
from football_schedule.schedules.forms import WeekForm, WeekEditForm, DisplayForm
from football_schedule.schedules.models import Week, DisplayScheduleData

# Create your views here.

class ScheduleCreateView(LoginRequiredMixin,DeleteCloudinaryFormValidMixin, View):
    template_name = 'schedules/schedule-create.html'
    success_url = reverse_lazy('create-schedule')

    def get_user_profile_data(self):
        user_profile = self.request.user.profile
        return {
            'club': user_profile.club,
            'club_emblem': user_profile.club_emblem if user_profile.club_emblem else None,
            'coach_photo': user_profile.profile_picture if user_profile.profile_picture else None,
            'team_generation_choice': user_profile.team_generation_choice,
            'team_generation': user_profile.team_generation,
            'coach': user_profile.get_full_name,
            'color': user_profile.color,
        }

    def get(self, request, *args, **kwargs):

        form = WeekForm()
        display_form = DisplayForm(initial=self.get_user_profile_data())

        context = {
            'form': form,
            'display_form': display_form,
            'weeks': Week.objects.filter(author=request.user).order_by('start_date'),
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        initial_display_data = self.get_user_profile_data()
        form = WeekForm()
        display_form = DisplayForm(initial=initial_display_data)

        if 'submit_form' in request.POST:
            form = WeekForm(request.POST)

            if form.is_valid():
                week = form.save(commit=False)
                week.author = request.user
                week.save()
                return redirect(self.success_url)

        elif 'submit_display_form' in request.POST:
            display_form = DisplayForm(request.POST, request.FILES, initial=initial_display_data)

            if display_form.is_valid():
                display_data = display_form.save(commit=False)
                display_data.user = request.user
                display_data.save()
                return redirect(reverse('display-schedule'))

        context = {
            'form': form,
            'display_form': display_form,
            'weeks': Week.objects.filter(author=request.user).order_by('id'),
        }
        return render(request, self.template_name, context)



class ScheduleDisplayView(LoginRequiredMixin,ListView):
    template_name = 'schedules/display-schedule.html'
    context_object_name = 'weeks'

    def get_queryset(self):
        return Week.objects.filter(author=self.request.user).order_by('id')

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        if DisplayScheduleData.objects.filter(user_id=self.request.user.id).count() > 1:
            DisplayScheduleData.objects.first().delete()

        display_data = DisplayScheduleData.objects.last()

        context['display_data'] = display_data

        return context

class ScheduleWeekEditView(LoginRequiredMixin,UpdateView):
    template_name = 'schedules/schedule-edit.html'
    form_class = WeekEditForm
    model = Week
    success_url = reverse_lazy('create-schedule')


class DeleteAllWeeksView(View):
    def post(self, request, *args, **kwargs):

        weeks_deleted, _ = Week.objects.filter(author=request.user).delete()
        messages.success(request, f"Successfully deleted {weeks_deleted} weeks.")

        return redirect('create-schedule')

def delete_week(request, pk):

    week = get_object_or_404(Week, pk=pk, author=request.user)
    week.delete()

    return redirect('create-schedule')




