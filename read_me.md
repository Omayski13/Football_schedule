# Football Schedule

Football Schedule is a Django web application designed for football coaches and club staff to organize weekly training schedules, manage match programs, and process attendance reports from Excel files. The application helps teams keep their planning in one place and export professional schedules and analytical reports.

## Overview

The system combines four main parts:

- Account and profile management for users and coaching staff
- Weekly training schedule creation and editing
- Match program creation and display
- Report generation from uploaded attendance files

The project is built with Django and designed for deployment in a production environment with PostgreSQL, Cloudinary media storage, and static file serving via WhiteNoise.

## Main Features

### 1. User accounts and profiles

- Custom user authentication using email as the username
- User registration and login
- Password reset flow
- Profile setup with:
  - first name and last name
  - club name
  - team generation
  - club emblem
  - coach photo
  - club colors
  - license information

### 2. Weekly training schedule management

Users can create and manage a weekly schedule for a team, including:

- Monday to Sunday planning
- Training type selection
- Time and place for each day
- Start date for each week
- Schedule editing and deletion
- Display of the final weekly calendar for the selected club
- Export to Excel for printing or sharing

### 3. Match program management

The app supports match-day planning by allowing the user to create a fixture list with:

- home team name
- away team name
- match date and time
- venue
- optional club emblems
- display of all matches in chronological order

### 4. Attendance report generation

One of the key functions of this app is report processing:

- Upload an Excel or XLSM attendance file
- Extract metadata such as club name, generation, and month
- Read training and match attendance data
- Generate summary charts and player-specific reports
- Download the processed results as a ZIP archive

This is especially useful for coaching staff who need to review attendance and participation trends without manually reviewing raw spreadsheet data.

## Project Structure

```text
Football_schedule/
├── football_schedule/
│   ├── accounts/          # User auth, profiles, password reset
│   ├── common/            # Shared utilities, home view, report processing logic
│   ├── programs/          # Match management and display
│   ├── reports/           # Excel report upload and processing
│   ├── schedules/         # Weekly scheduling functionality
│   ├── settings.py        # Django project settings
│   ├── urls.py            # Root URL configuration
│   └── ...
├── requirements.txt
├── manage.py
├── venv/
├── LICENSE
└── README.md
```

## Technology Stack

This application uses the following technologies:

- Python
- Django 5.1.4
- PostgreSQL (configured through `dj-database-url`)
- Cloudinary for media storage
- WhiteNoise for static files in production
- Python-Decouple for environment configuration
- Pandas for Excel data processing
- OpenPyXL for spreadsheet reading/writing
- Matplotlib for chart generation
- Gunicorn for serving the app in production
- SMTP email backend for password reset and notifications

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@host:5432/dbname
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=no-reply@example.com
```

Note: the project is configured to run in a deployment environment such as Render, so the `ALLOWED_HOSTS` includes `.onrender.com`.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Omayski13/Football_schedule.git
cd Football_schedule
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the environment variables in a `.env` file.

5. Run database migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

The app will be available at:

```text
http://127.0.0.1:8000/
```

## Administration

The project includes Django admin support:

```bash
python manage.py createsuperuser
```

After that, you can access the admin panel at:

```text
http://127.0.0.1:8000/admin/
```

## Use Cases

This app is useful for:

- football academies
- youth teams and junior squads
- coaches managing weekly practice plans
- clubs handling match calendars
- staff analyzing team attendance trends

## License

This project is distributed under the MIT license. See the LICENSE file for details.

## Notes

The application is tailored specifically for football team scheduling and reporting, with the ability to generate training plans and club-specific documents from structured data. It is suitable for organizations that want a centralized digital workflow for managing team activities and attendance reporting.
