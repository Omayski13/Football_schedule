from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, FormView

from football_schedule.schedules.forms import WeekForm, WeekEditForm, DisplayForm
from football_schedule.schedules.models import Week, DisplayScheduleData


# Create your views here.

class ScheduleCreateView(View):
    template_name = 'schedules/schedule-create.html'
    success_url = reverse_lazy('create-schedule')

    def get_user_profile_data(self):
        """
        Helper method to get initial data for the DisplayForm based on the user's profile.
        """
        user_profile = self.request.user.profile
        return {
            'club_emblem': user_profile.club_emblem.url if user_profile.club_emblem else None,
            'coach_photo': user_profile.profile_picture.url if user_profile.profile_picture else None,
            'generation': user_profile.generation,
            'coach': user_profile.get_full_name,
        }

    def get(self, request, *args, **kwargs):
        # Initialize forms
        form = WeekForm()
        display_form = DisplayForm(initial=self.get_user_profile_data())

        # Prepare context
        context = {
            'form': form,
            'display_form': display_form,
            'weeks': Week.objects.filter(author=request.user),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Get user profile data for DisplayForm initialization
        initial_display_data = self.get_user_profile_data()

        # Initialize forms with default or posted data
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
            # Include request.FILES to handle file uploads
            display_form = DisplayForm(request.POST, request.FILES, initial=initial_display_data)
            if display_form.is_valid():
                display_data = display_form.save(commit=False)
                display_data.user = request.user
                display_data.save()
                return redirect(reverse('display-schedule'))  # Redirect to 'display-schedule'

        # Re-render the page with errors if forms are invalid
        context = {
            'form': form,
            'display_form': display_form,
            'weeks': Week.objects.filter(author=request.user),
        }
        return render(request, self.template_name, context)





# class ScheduleCreateView(CreateView):
#     template_name = 'schedules/schedule-create.html'
#     form_class = WeekForm
#     model = DisplayScheduleData
#     success_url = reverse_lazy('create-schedule')
#
#     def form_valid(self, form):
#         # First, handle saving the week object
#         week = form.save(commit=False)
#         week.author = self.request.user  # Assign the logged-in user
#         week.save()  # Save the week instan
#
#         display_form = DisplayForm(self.request.POST or None)
#         if display_form.is_valid():
#             # Save the display data to DisplayScheduleData model
#             display_data = display_form.save(commit=False)
#             display_data.user = self.request.user  # Link the user to the display data
#             display_data.save()  # Save the data to the database
#             print("Display data saved successfully!")  # Debugging line
#         else:
#             print("DisplayForm is not valid:", display_form.errors)  # Debugging line
#
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         # Get the user's profile and populate the DisplayForm
#         user_profile = self.request.user.profile
#
#         context['weeks'] = Week.objects.filter(author=self.request.user)
#         context['display_form'] = DisplayForm(initial={
#             'club_emblem': user_profile.club_emblem.url if user_profile.club_emblem else None,
#             'coach_photo': user_profile.profile_picture.url if user_profile.profile_picture else None,
#             'generation': user_profile.generation,
#             'coach': user_profile.get_full_name,
#         })
#
#         return context




class ScheduleDisplayView(ListView):
    template_name = 'schedules/display.html'
    context_object_name = 'weeks'

    def get_queryset(self):
        return Week.objects.filter(author=self.request.user)

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)

        if DisplayScheduleData.objects.filter(user_id=self.request.user.id).count() > 1:
            DisplayScheduleData.objects.first().delete()

        display_data = DisplayScheduleData.objects.last()

        # Add DisplayScheduleData to the context
        context['display_data'] = display_data


        return context

class ScheduleWeekEditView(UpdateView):
    template_name = 'schedules/schedule-edit.html'
    form_class = WeekEditForm
    model = Week
    success_url = reverse_lazy('create-schedule')



class DeleteAllWeeksView(View):
    def post(self, request, *args, **kwargs):
        # Delete all weeks created by the logged-in user
        weeks_deleted, _ = Week.objects.filter(author=request.user).delete()
        messages.success(request, f"Successfully deleted {weeks_deleted} weeks.")
        return redirect('create-schedule')  # Redirect to a relevant page

def delete_week(request, pk):
    week = get_object_or_404(Week, pk=pk, author=request.user)  # Ensure user owns the week
    week.delete()
    return redirect('create-schedule')  # Redirect to the list view or another appropriate page




