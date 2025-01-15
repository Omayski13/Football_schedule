from django.contrib import admin

from football_schedule.schedules.models import Week, DisplayScheduleData


# Register your models here.

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    pass


@admin.register(DisplayScheduleData)
class DisplayScheduleDataAdmin(admin.ModelAdmin):
    pass
