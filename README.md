# ⚽Football Schedule

Football Schedule is a Django-based web application for football coaches and team staff to manage training schedules, maintain club profiles, and generate attendance reports from Excel files. The app is designed to simplify daily planning, improve communication with players, and provide a clear overview of team activity in one place.

This project combines football team management with an ETL and analytics workflow for processing attendance reports from Excel files.

### 🌐Deployment
You can view the live version of the project here: [Live Demo](https://football-schedule.onrender.com/). <br>
<strong>*Note:</strong> The application is hosted on a free-tier service. The first load may **take a few minutes** while the server wakes up.

# 📖Overview

The system combines four main parts:

- Account and profile management for users and coaching staff
- Weekly training schedule creation and editing
- Match program creation and display
- Report generation from uploaded attendance files

The project is built using **Django** and designed for deployment in a production environment.
 
### Backend
- Django (Python)
- PostgreSQL database
- Pandas & OpenPyXL for data processing
 
### Media Storage
- Cloudinary for storing and serving uploaded media files, including club emblems, coach photos, and generated assets
 
### Deployment
- Hosted on Render
- Production-ready configuration with environment variables and secure settings
- PostgreSQL integration for persistent data storage
 

# 🌟Features

##  👤 1. User Accounts & Profiles setup
### User Account

The platform provides a complete authentication and profile management system for football clubs and coaches.

**Features:**
  - Custom user authentication using email as the username
  - User registration and login
  - Password reset functionality

###  Club Profile Setup
Users can configure their club profile with:

- First and last name
- Club name
- Team generation (age group)
- Club emblem
- Coach photo
- Club colors
- License information

## 📊 2. Report Processing & Analytics Pipeline

One of the core functionalities of the application is automated report processing. The pipeline transforms raw attendance data into structured analytics and downloadable outputs.

### Step 1: Data Input
- Upload an Excel file containing attendance data for training sessions and matches
- Store the file temporarily on the server
- Process data in the backend rather than directly in the user interface

### Step 2: Pipeline Initialization
- Create a processing job with a unique identifier
- Send the uploaded file to the processing pipeline
- Execute processing asynchronously to keep the UI responsive

### Step 3: Data Loading
- Read Excel files using **Pandas** and **OpenPyXL**
- Analyze worksheet structure
- Identify relevant rows and columns
- Load data into a DataFrame for processing

### Step 4: Metadata Extraction
The system extracts key contextual information such as:

- Club name
- Team generation
- Month
- Reporting season or period

This metadata provides the context required for accurate reporting and output generation.

### Step 5: Data Cleaning & Normalization
- Detect training and match dates
- Extract player information
- Process attendance and absence indicators
- Convert raw data into analysis-ready structures
- Validate file formats and identify anomalies

### Step 6: KPI Calculation
The following metrics are calculated automatically:

- Total training sessions
- Attendance and absence counts
- Average attendance per player
- Participation trends by day and reporting period
- Separate statistics for training and match activities

These KPIs support performance evaluation and reporting.

### Step 7: Visualization & Chart Generation
- Generate attendance charts using Matplotlib
- Create individual player visualizations when required
- Present results in a clear and user-friendly format

### Step 8: Output Generation
- Produce charts and analytical summaries
- Package processed data and visual assets
- Generate a downloadable ZIP archive

### ⚙️Data pipeline architecture

```text
Excel/XLSM file
    ↓
Django upload endpoint
    ↓
Background job / async processing
    ↓
Data loading with pandas/openpyxl
    ↓
Metadata extraction + cleaning
    ↓
Business rules + KPI calculations
    ↓
Chart generation with Matplotlib
    ↓
ZIP archive / downloadable report
```

### ▶️Instructions how to start the pipeline
Detailed istructions how to start the pipeline in English and Bulgarian:
- [Instructions EN](https://github.com/Omayski13/Football_schedule/blob/main/documents/REPORT_INSTRUCTIONS_EN.md)
- [Instructions BG](https://github.com/Omayski13/Football_schedule/blob/main/documents/REPORT_INSTRUCTIONS_BG.md)

## 🗓️ 3. Weekly Training Schedule Management

Users can create and manage weekly schedules for their teams.

### 1. Schedule Capabilities
- Planning from Monday through Sunday
- Training type selection
- Time and location assignment
- Weekly start date configuration
- Schedule editing and deletion

### 2. Output
- Calendar view of the weekly training plan
- Club-specific schedule display
- Excel export for printing and sharing


# 📁Project Structure

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

# 🛠️Technology Stack

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

# 🔑Environment Variables

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

# 📋Requirements

- Python 3.10+
- pip
- PostgreSQL database
- Cloudinary account
- SMTP email configuration

# 🚀Installation

1. Clone the repository:

```terminal
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


# 🎯Use Cases

This app is useful for:

- football academies
- youth teams and junior squads
- coaches managing weekly practice plans
- clubs handling match calendars
- staff analyzing team attendance trends

# ⚖️License

This project is distributed under the MIT license. See the [LICENSE](https://github.com/Omayski13/Football_schedule/blob/main/LICENSE) file for details.
