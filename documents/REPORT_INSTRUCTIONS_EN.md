# Report Generation Instructions

Use this feature to generate monthly reports on attendance at training sessions and matches. The results include team-level summaries and individual statistics for each player, presented as charts.

## What the report contains

### Training sessions

- Number of training sessions during the month
- Number of players who attended training during the month
- Average attendance per session — the average number of players present
- Total attendance and absence counts and percentages

### Matches

- Number of matches during the month
- Number of players who participated in matches during the month
- Total attendance and absence counts and percentages

### Individual performance

For each player, the report shows:

- Number of training attendances and absences
- A chart and percentages for training attendance and absences
- Dates of training attendance and absences
- Number of match attendances and absences
- A chart and percentages for match attendance and absences
- Dates of match attendance and absences

![Individual player information](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/player_info.png)

![Match information](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/matches_info.png)

![Training information](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/trainings_info.png)

## 1. Download the template

1. Open the report generation page.
2. Click the **„Свали Шаблон“** button (Download Template).
3. After downloading, find the Excel file in your browser's downloads folder.
4. Open the file and fill in the team information in the header rows.
5. Add the club emblem, then position and resize it as needed.

![Download the template](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/download-template.png)

## 2. Enter the players

You can add up to 23 players to the template.

- Enter player names in the **„Футболист“** (Player) column.
- Enter shirt numbers in the **„№“** (No.) column. If you do not use shirt numbers, keep the default sequence from 1 to 23.
- The **„Общо“** (Total) row below the player list shows the number of players added.

![Enter players](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/populate-players.png)

## 3. Enter training attendance

For each training session, enter its date and attendance data:

- In the gray row after **„дата“** (date), enter the training dates for the relevant month. Enter only the day; the month is determined automatically when the report is generated.
- For each player, enter **1** for present and **0** for absent.
- The template automatically colors cells to indicate attendance or absence.
- The row below the attendance data shows the total number of players present at each session.
- The **„Участия“** (Attendances) and **„Отсъствия“** (Absences) columns show each player's total attendance and absence counts.

![Enter training attendance](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/populate-absence.png)

## 4. Enter match attendance

For each match, enter its date and player participation data:

- In the blue row after **„дата“** (date), enter match dates for the relevant month. Enter only the day; the month is determined automatically when the report is generated.
- For each player, enter **1** for present and **0** for absent.
- The template automatically colors cells to indicate attendance or absence.
- The row below the attendance data shows the total number of players present at each match.
- The **„Участия Мачове“** (Match Participation) column shows each player's total match participations and absences.

![Enter match attendance](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/populate-matches.png)

## 5. Generate and download the report

1. Under **„Качи попълнен файл:“** (Upload completed file), click **„Choose File“**.
2. Find and select the completed Excel template.
3. Check that the selected file name appears next to **„Choose File“**.
4. Click **„Генерирай репорт“** (Generate Report).
5. You will be redirected to a processing page. The message **„Файлът се обработва и свалянето ще започне скоро“** means the report is being generated.
6. When processing is complete, a ZIP file containing the results will start downloading automatically.
7. To create another report, click **„Генерирай нов репорт“** (Generate New Report).

![Upload the completed file](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/generate-report-1.png)

![Report processing](https://github.com/Omayski13/Football_schedule/blob/main/football_schedule/static/images/generate-report-2.png)

## Processing summary

The completed Excel template contains team, player, date, and attendance data. After upload, the system processes the data and generates monthly summaries and individual chart reports. The results are provided to the user as a ZIP archive.
