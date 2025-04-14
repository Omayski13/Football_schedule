from datetime import timedelta

from django.views.generic import TemplateView

import pandas as pd
from django.http import HttpResponse
from openpyxl import load_workbook
from openpyxl.styles import Border, Side, Font, PatternFill, Alignment
from io import BytesIO


from football_schedule.schedules.models import Week, DisplayScheduleData


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


def download_schedule_excel(request):
    # Fetch the schedule data for the logged-in user
    weeks = Week.objects.filter(author=request.user).order_by('id')

    # Prepare data for DataFrame
    data = []
    schedule_date = DisplayScheduleData.objects.last()
    data.append([schedule_date.club])
    data.append([schedule_date.team_generation])
    data.append([f"треньор {schedule_date.coach}"])
    data.append([f"Месец {schedule_date.month}"])

    for week in weeks:
        week_dates = [
            f"{week.start_date.strftime('%d.%m')}-{(week.start_date + timedelta(days=6)).strftime('%d.%m')}"
        ]
        # First row: Days of the week
        days_of_week = [
            "П", "В", "С", "Ч", "П", "С", "Н"
        ]

        types = [
            week.monday_type,
            week.tuesday_type,
            week.wednesday_type,
            week.thursday_type,
            week.friday_type,
            week.saturday_type,
            week.sunday_type,
        ]

        # Second row: Times for each day
        times = [
            f"{week.monday_time.strftime('%H:%M')} часа" if week.monday_time else "",
            f"{week.tuesday_time.strftime('%H:%M')} часа" if week.tuesday_time else "",
            f"{week.wednesday_time.strftime('%H:%M')} часа" if week.wednesday_time else "",
            f"{week.thursday_time.strftime('%H:%M')} часа" if week.thursday_time else "",
            f"{week.friday_time.strftime('%H:%M')} часа" if week.friday_time else "",
            f"{week.saturday_time.strftime('%H:%M')} часа" if week.saturday_time else "",
            f"{week.sunday_time.strftime('%H:%M')} часа" if week.sunday_time else "",
        ]

        # Third row: Places for each day
        places = [
            week.monday_place if week.monday_place else "",
            week.tuesday_place if week.tuesday_place else "",
            week.wednesday_place if week.wednesday_place else "",
            week.thursday_place if week.thursday_place else "",
            week.friday_place if week.friday_place else "",
            week.saturday_place if week.saturday_place else "",
            week.sunday_place if week.sunday_place else "",
        ]

        # Add the rows to data
        data.append(week_dates)
        data.append(days_of_week)
        data.append(types)
        data.append(times)
        data.append(places)

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create an in-memory buffer to store the Excel file
    output = BytesIO()

    # Save DataFrame to Excel in memory
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Schedule", index=False, header=False)  # Do not include index or header

    # Load the workbook from the in-memory buffer
    output.seek(0)
    wb = load_workbook(output)
    ws = wb.active  # Get the active sheet (Schedule)

    merged_rows = [1,2,3,4,5,10,15,20,25]
    date_fill = PatternFill(start_color="0066ff",end_color="0066ff", fill_type="solid")
    day_fill = PatternFill(start_color="80b3ff",end_color="80b3ff", fill_type="solid")

    for row in merged_rows:
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=7)
        if row > 4:
            ws.cell(row=row, column=1).fill = date_fill
            for c in range(1,8):
                ws.cell(row=row, column=c).fill = day_fill

    # Define border style
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # Apply border and center alignment to all cells
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        for cell in row:
            cell.border = thin_border
            cell.alignment = Alignment(horizontal="center", vertical="center")

    # Save the styled workbook back to the in-memory buffer
    output = BytesIO()
    wb.save(output)
    output.seek(0)

    # Create HTTP response
    response = HttpResponse(
        output.getvalue(),
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="schedule.xlsx"'

    return response



