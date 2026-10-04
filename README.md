# Football Schedule

Football Schedule is a Django-based web application for football coaches and team staff to manage training schedules, maintain club profiles, and generate attendance reports from Excel files.

The app is designed to simplify daily planning, improve communication with players, and provide a clear overview of team activity in one place.

## Features

- User registration, login, and profile setup
- Club information and team configuration
- Weekly football training schedule creation and editing
- Schedule display for a selected team and month
- Excel export of schedule data
- Attendance report processing from uploaded files
- Visual analytics and player attendance summaries
- Password reset flow for authenticated users
- Cloudinary-based media storage for club emblems and coach photos

## Tech Stack

- Python
- Django 5.1.4
- PostgreSQL
- Cloudinary
- WhiteNoise
- Pandas
- OpenPyXL
- Matplotlib
- Django email backend
- python-decouple

## Project Structure

```text
Football_schedule/
├── football_schedule/
│   ├── accounts/        # User accounts, profiles, and auth logic
│   ├── common/          # Shared views and report-processing utilities
│   ├── reports/         # Report upload and result generation
│   ├── schedules/       # Weekly schedule management and display
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main application routing
│   └── ...
├── requirements.txt
├── manage.py
├── LICENSE
├── README.md
└── venv/
```

## Requirements

- Python 3.10+
- pip
- PostgreSQL database
- Cloudinary account
- SMTP email configuration

## Environment Variables

Create a `.env` file in the project root with the following values:

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

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Omayski13/Football_schedule.git
cd Football_schedule
```

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your `.env` file.

5. Apply migrations:

```bash
python manage.py migrate
```

6. Start the application:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Admin Panel

Create an admin user:

```bash
python manage.py createsuperuser
```

Then access:

```text
http://127.0.0.1:8000/admin/
```

## Usage

The app is intended for football organizations that need to:

- organize training week plans
- update coach and club information
- manage a team calendar
- export schedule data for external use
- process attendance statistics from Excel files

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Notes

This project is tailored to football team management and works best for coaches, staff, and youth football organizations that want a centralized system for planning and reporting.

