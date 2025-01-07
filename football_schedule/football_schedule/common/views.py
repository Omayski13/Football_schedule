from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from football_schedule.schedules.models import Week, DisplayScheduleData


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

