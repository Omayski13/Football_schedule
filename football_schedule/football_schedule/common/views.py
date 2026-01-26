from datetime import timedelta

import matplotlib
matplotlib.use("Agg")

from django.views.generic import TemplateView

import os
import zipfile
import tempfile
import matplotlib.pyplot as plt
import re
import math
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


def process_xlsm(input_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    absence_file = pd.read_excel(input_path, engine='openpyxl')

    output_path = os.path.join(output_dir, "01_")
    os.makedirs(output_path, exist_ok=True)


    all_dates = absence_file.iloc[4, 3:]
    training_dates = all_dates[0:15].dropna().tolist()
    match_dates = all_dates[16:21].dropna().tolist()

    players_count = absence_file.iloc[5:28, 1].dropna().tolist()

    club_name = absence_file.columns[3]
    generation = absence_file.iloc[0, 3]
    month = absence_file.iloc[1, 3]

    # ********** MONTH

    MONTH_MAP = {
        "януари": "януари", "ян": "януари", "яну": "януари",
        "january": "януари", "jan": "януари",

        "февруари": "февруари", "фев": "февруари", "февр": "февруари",
        "february": "февруари", "feb": "февруари",

        "март": "март", "мар": "март",
        "march": "март", "mar": "март",

        "април": "април", "апр": "април",
        "april": "април", "apr": "април",

        "май": "май",
        "may": "май",

        "юни": "юни", "юн": "юни",
        "june": "юни", "jun": "юни",

        "юли": "юли", "юл": "юли",
        "july": "юли", "jul": "юли",

        "август": "август", "авг": "август",
        "august": "август", "aug": "август",

        "септември": "септември", "сеп": "септември", "септ": "септември",
        "september": "септември", "sep": "септември", "sept": "септември",

        "октомври": "октомври", "окт": "октомври",
        "october": "октомври", "oct": "октомври",

        "ноември": "ноември", "ное": "ноември", "ноем": "ноември",
        "november": "ноември", "nov": "ноември",

        "декември": "декември", "дек": "декември",
        "december": "декември", "dec": "декември",
    }

    MONTH_MAP_STR_TO_INT = {
        "януари": "01",
        "февруари": "02",
        "март": "03",
        "април": "04",
        "май": "05",
        "юни": "06",
        "юли": "07",
        "август": "08",
        "септември": "09",
        "октомври": "10",
        "ноември": "11",
        "декември": "12",
    }

    month = month.strip().lower()
    month_num = None
    month_parts = re.split(r"[\s\.,;:/\-]+", month)
    for part in month_parts:
        if part in MONTH_MAP:
            month = MONTH_MAP[part]
            month_num = MONTH_MAP_STR_TO_INT[month]

    training_df = absence_file.iloc[5:28, 1:19]
    training_df.columns = absence_file.iloc[4, 1:19]
    training_df = training_df.drop(training_df.columns[1], axis=1)

    block = training_df.iloc[0:24, 1:16]

    if not training_dates:
        print("no data inputed for training")

    elif not players_count:
        print("no data inputed for players ")

    else:
        trainings_count = (training_df.iloc[0].count()) - 1
        absence_count = (block == 0).sum().sum()
        presence_count = (block == 1).sum().sum()
        avg_players_on_training = round(presence_count / trainings_count)

    if not training_dates:
        print("no data inputed for training")

    elif not players_count:
        print("no data inputed for players ")

    else:
        labels = ['Отсъстващи', 'Присъстващи']
        values = [absence_count, presence_count]

        fig, ax = plt.subplots(figsize=(8, 8))

        def autopct_format(pct, all_vals):
            absolute = int(round(pct / 100. * sum(all_vals)))
            return f"{pct:.0f}%\n({absolute})"

        wedges, texts, autotexts = ax.pie(
            values,
            autopct=lambda pct: autopct_format(pct, values),
            startangle=90,
            colors=["#c21919", "#43c01d"]
        )

        for autotext in autotexts:
            autotext.set_fontsize(12)

        ax.set_title(f"{club_name}\n{generation}\nмесец {month}")

        ax.legend(wedges, labels, loc="upper right")

        ax.text(
            0.5, 0.05,
            f"Общо тренировки за месеца: {trainings_count}\n"
            f"Общо деца: {len(players_count)}\n"
            f"Средно деца на тренировка: {avg_players_on_training}",
            ha='center', va='center',
            fontsize=12, color='black',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=5),
            transform=ax.transAxes
        )

        export_path = f"{output_path}Информация_тренировки_{month}.png"
        plt.savefig(export_path, dpi=300, bbox_inches='tight')


    if not match_dates:
        print("no data inputed for matches")

    elif not players_count:
        print("no data inputed for players ")

    else:

        match_df = absence_file.iloc[5:28, 1:24]
        match_df.columns = absence_file.iloc[4, 1:24]
        match_df = match_df.iloc[:, [0] + list(range(18, 23))]

        block_match = match_df.iloc[0:24, 1:6]

        # matches_dates = block_match.loc[:1, block_match.columns.notna()]
        match_absence_count = (block_match == 0).sum().sum()
        match_presence_count = (block_match == 1).sum().sum()

        matches = {}

        for match_counter, cols in zip(range(1, (len(matches_dates.columns) + 1)),
                                       range(1, (len(matches_dates.columns)) + 1)):
            match_count_block = match_df.iloc[0:24, (0 + cols):(1 + cols)]

            if match_counter not in matches:
                matches[match_counter] = []
                matches[match_counter].append(matches_dates.columns[cols - 1])
                players_for_match = int((match_count_block == 1).sum().sum())
                matches[match_counter].append(players_for_match)

    if not match_dates:
        print("no data inputed for matches")

    elif not players_count:
        print("no data inputed for players ")

    else:
        colors = ["#c21919", "#B8CCE4"]
        labels = ['Отсъстващи', 'Присъстващи']

        num_matches = len(matches)
        right_ncols = min(3, max(1, int(math.ceil(math.sqrt(num_matches)))))  # cap at 3 cols for readability
        right_nrows = int(math.ceil(num_matches / right_ncols))

        fig = plt.figure(figsize=(6 + 4 * right_ncols, 4.5 * max(1, right_nrows)))  # scale with grid
        outer = fig.add_gridspec(nrows=max(1, right_nrows), ncols=2, width_ratios=[1.2, 2.0], wspace=0.25)

        # ----- LEFT: BIG SUMMARY PIE -----
        summary_ax = fig.add_subplot(outer[:, 0])
        summary_values = [match_absence_count, match_presence_count]

        def make_autopct(values, show_percent=False):
            """Returns a function for autopct that prints counts (and optionally %)."""
            total = sum(values)

            def _fmt(pct):
                val = int(round(pct * total / 100.0))
                return f"{pct:.0f}% ({val})" if show_percent else f"{val}"

            return _fmt

        wedges, texts, autotexts = summary_ax.pie(
            summary_values,
            # labels=labels,
            autopct=make_autopct(summary_values, show_percent=True),  # True -> shows "value (percent)"
            startangle=90,
            colors=colors,
            textprops={'fontsize': 11}
        )

        summary_ax.legend(wedges, labels, loc="upper right")

        summary_ax.set_title(f"Информация за всички мачове\nМесец {month}", fontsize=14, pad=12)

        summary_ax.text(
            0.5, 0.05,
            f"Общо присъствали: {match_presence_count}\nОбщо отсъствали: {match_absence_count}",
            ha='center', va='center',
            fontsize=11, color='black',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=5),
            transform=summary_ax.transAxes
        )

        # ----- RIGHT: GRID WITH SMALL PIES PER MATCH -----
        right = outer[:, 1].subgridspec(nrows=right_nrows, ncols=right_ncols, hspace=0.35, wspace=0.30)

        axes = [fig.add_subplot(right[i, j]) for i in range(right_nrows) for j in range(right_ncols)]

        for ax, (match, info) in zip(axes, matches.items()):
            present = info[1]
            absent = len(players_count) - present
            values = [absent, present]

            ax.pie(
                values,
                autopct=make_autopct(values, show_percent=True),  # counts only
                startangle=90,
                colors=colors,
                textprops={'fontsize': 9}
            )
            ax.set_title(f"Мач №{match} — {info[0]} {month}", fontsize=10)

            ax.text(
                0.5, 0.05,
                f"Присъствали: {present}\nОтсъствали: {absent}",
                ha='center', va='center',
                fontsize=6, color='black',
                bbox=dict(facecolor='white', alpha=0.65, edgecolor='none', pad=3),
                transform=ax.transAxes
            )

        for i in range(num_matches, len(axes)):
            axes[i].axis('off')

        plt.tight_layout()

        export_path = f"{output_path}Информация_мачове_{month}.png"
        plt.savefig(export_path, dpi=300, bbox_inches='tight')

        # PLAYERS INFO FOR TRAININGS AND MATCHES

    players_df = absence_file.iloc[5:28, 1:24].copy()  # slice players rows
    players_df = players_df.drop(players_df.columns[1], axis=1)  # drop unwanted column
    players_df.reset_index(drop=True, inplace=True)  # ensure positional indexing

    for index, player in enumerate(players_count):
        player_row = players_df.iloc[index]
        player_name = str(player_row.iloc[0])  # make sure it's a string

        if not player_name or player_name.lower() == 'nan':
            continue

        if player != player_name:
            continue

        player_trainings = (
            player_row.iloc[1:16]
            .fillna(0)
            .infer_objects()  # lets pandas infer proper dtype
            .astype(int)
            .tolist()
        )

        player_matches = (
            player_row.iloc[16:]
            .fillna(0)
            .infer_objects()
            .astype(int)
            .tolist()
        )

        # TRAINING AND MATCH DATA

        training_presence_dates = []
        training_absence_dates = []
        match_presence_dates = []
        match_absence_dates = []

        def populate(event_data, event_dates, presence_list, absence_list, month_num):
            for i, event in enumerate(event_data):
                if i >= len(event_dates):
                    continue
                if event == 1:
                    presence_list.append(f"{event_dates[i]}.{month_num}")
                elif event == 0:
                    absence_list.append(f"{event_dates[i]}.{month_num}")

        if training_dates:
            populate(player_trainings, training_dates, training_presence_dates, training_absence_dates, month_num)
        if match_dates:
            populate(player_matches, match_dates, match_presence_dates, match_absence_dates, month_num)

        pies_to_draw = []
        if training_dates:
            pies_to_draw.append(("тренировки", training_presence_dates, training_absence_dates, "#43c01d"))
        if match_dates:
            pies_to_draw.append(("мачове", match_presence_dates, match_absence_dates, "#B8CCE4"))

        if not pies_to_draw:
            continue

        fig, axes = plt.subplots(1, len(pies_to_draw), figsize=(8 * len(pies_to_draw), 8))
        if len(pies_to_draw) == 1:
            axes = [axes]

        fig.suptitle(f"{player_name}", fontsize=18, fontweight='bold')

        def autopct_format(pct, all_vals):
            absolute = int(round(pct / 100.0 * sum(all_vals)))
            return f"{pct:.0f}%\n({absolute})"

        for ax, (event_type, presence, absence, color_presence) in zip(axes, pies_to_draw):
            values = [len(absence), len(presence)]
            wedges, texts, autotexts = ax.pie(
                values,
                autopct=lambda pct: autopct_format(pct, values),
                startangle=90,
                colors=["#c21919", color_presence]
            )
            ax.set_title(f"{event_type} за месец {month}")
            ax.legend(wedges, ['Отсъствия', 'Присъствия'], loc="upper right")

            summary = [f"Общо {event_type}: {sum(values)}"]
            if presence:
                summary.append(f"Присъствия: {', '.join(presence)} - общо {len(presence)}")
            if absence:
                summary.append(f"Отсъствия: {', '.join(absence)} - общо {len(absence)}")
            ax.text(0.5, 0.1, "\n".join(summary), ha='center', va='top',
                    fontsize=11, transform=ax.transAxes)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        export_file = os.path.join(output_path, f"{player_name}_Информация_{month}_месец.png")
        plt.savefig(export_file, dpi=300, bbox_inches='tight')
        plt.close()

    return output_dir


