from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from football_schedule.programs.forms import MatchCreateForm, MatchEditForm, DisplayProgramForm
from football_schedule.programs.models import Match, DisplayProgramData


class CreateMatchView(LoginRequiredMixin, View):
    template_name = 'programs/create-program.html'
    success_url = reverse_lazy('create-program')

    def get_user_profile_data(self):
        """ Fetch initial data for the DisplayProgramForm from the user's profile. """
        user_profile = getattr(self.request.user, 'profile', None)
        return {
            'club': user_profile.club if user_profile else '',
            'club_emblem': user_profile.club_emblem if user_profile and user_profile.club_emblem else None,
        }

    def get_context_data(self, **kwargs):
        """ Prepare context for rendering the page. """
        context = kwargs
        context.setdefault('form', MatchCreateForm())
        context.setdefault('display_program_form', DisplayProgramForm(initial=self.get_user_profile_data()))
        context['matches'] = Match.objects.filter(author=self.request.user).order_by('date', 'time')
        return context

    def get(self, request, *args, **kwargs):
        """ Handle GET request and render the page. """
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get("form_type")  # Identify which form was submitted

        if form_type == "display_program_form":
            display_program_form = DisplayProgramForm(request.POST, request.FILES)

            if display_program_form.is_valid():
                display_program = display_program_form.save(commit=False)
                display_program.user = request.user  # Assign the user

                # 🛠 Check if "Изчисти" (Clear) is ticked
                if "club_emblem-clear" in request.POST:
                    display_program.club_emblem = None  # Clear the emblem

                # 🛠 If no new emblem is uploaded and "Изчисти" is NOT checked, keep the old emblem
                elif not request.FILES.get("club_emblem"):
                    user_profile = getattr(request.user, 'profile', None)
                    if user_profile:
                        display_program.club_emblem = user_profile.club_emblem  # Keep profile emblem

                display_program.save()
                return redirect(reverse('display-program'))  # Redirect after saving

            # If form has errors, re-render the page
            return render(request, self.template_name, self.get_context_data(display_program_form=display_program_form))

        return redirect(self.success_url)  # Default redirect



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

class DisplayProgramView(LoginRequiredMixin,ListView):
    template_name = 'programs/display-program.html'
    model = Match


    def get_queryset(self):

        queryset = Match.objects.filter(author=self.request.user).order_by('date','time')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if DisplayProgramData.objects.filter(user_id=self.request.user.id).count() > 1:
            DisplayProgramData.objects.first().delete()

        dates = []
        matches = Match.objects.filter(author=self.request.user).order_by('date','time')
        for match in matches:
            if match.date not in dates:
                dates.append(match.date)

        first_date = dates[0]
        last_date = dates[-1] if len(dates) > 1 else None

        context['dates'] = dates
        context['display_program_data'] = DisplayProgramData.objects.filter(user_id=self.request.user.id).first()
        context['first_date'] = first_date
        context['last_date'] = last_date

        return context

