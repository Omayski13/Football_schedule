from django.views.generic import TemplateView


from football_schedule.schedules.models import Week, DisplayScheduleData


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
