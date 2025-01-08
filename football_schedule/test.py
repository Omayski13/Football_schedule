from football_schedule.schedules.models import DisplayScheduleData

schedules = DisplayScheduleData.objects.last()

schedules.id