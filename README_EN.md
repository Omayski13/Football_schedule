# Football Schedule

Football Schedule is a Django-based project that combines football team management with an ETL and analytics workflow for processing attendance reports from Excel files.

This project was designed not only as a tool for coaches and administrators, but also as a portfolio project for Data Analyst and Data Engineer roles. It demonstrates how raw spreadsheet data can be collected, transformed, analyzed, visualized, and turned into useful business-ready output.

## What this project demonstrates

- Working with Excel and XLSM files as input data sources
- Extracting and normalizing metadata from tabular files
- Building an ETL-like data processing pipeline
- Analyzing player attendance and participation trends
- Calculating business KPIs and aggregated metrics
- Visualizing results using charts and reports
- Generating downloadable output packages for users

## Main focus: Data pipeline for report processing

The project includes a dedicated report-processing workflow that handles uploaded attendance files. The full process is structured as follows:

### 1. Input data
- A user uploads an Excel file containing attendance information for training sessions and matches
- The file is submitted to a Django view and temporarily stored on the server
- The data is processed in the backend rather than directly in the UI

### 2. Pipeline initialization
- The application creates a processing job with a unique identifier
- The file is sent to a background processing function
- The task runs asynchronously so the user interface remains responsive

### 3. Loading the data
- The Excel file is read with pandas and openpyxl
- The sheet structure is analyzed to identify relevant columns and rows
- The data is loaded into a DataFrame for structured processing

### 4. Metadata extraction
- Club name
- Team generation
- Month
- Reporting period/season

This step provides the context needed to properly interpret and format the final outputs.

### 5. Cleaning and normalization
- Detecting training and match dates
- Extracting the list of players
- Handling presence/absence values
- Converting raw data into analysis-friendly structures
- Validating file format and identifying anomalies

### 6. KPI calculation
- Total number of training sessions
- Attendance and absence counts
- Average attendance per player
- Participation trends by day and period
- Separate analysis for training and match data

These metrics support reporting, evaluation, and performance analysis.

### 7. Chart generation and visualization
- Matplotlib is used to produce attendance and participation charts
- Individual charts are generated for players when needed
- Results are displayed in a clear and understandable format

### 8. Output creation
- Charts and results are generated
- Processed data is packaged
- A ZIP archive is created for download by the user

This reflects a typical data engineering and analytics workflow: from raw file to structured, visualized, and usable output.

## What is implemented in the project

### Team and schedule management
- User profiles and coach information
- Club details, emblems, and media assets
- Weekly training schedule creation and editing
- Schedule display for a selected period
- Excel export of schedule data

### Attendance data analysis
- Processing Excel attendance reports
- Separating training and match data
- Calculating per-player statistics
- Visualizing attendance outcomes
- Providing quick access to generated reports

## Technical stack

- Python
- Django 5.1.4
- PostgreSQL
- Pandas
- OpenPyXL
- Matplotlib
- Cloudinary
- WhiteNoise
- Python-decouple
- Gunicorn
- SMTP email backend

## Data pipeline architecture

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

## Project structure

```text
Football_schedule/
├── football_schedule/
│   ├── accounts/        # users, profiles, and authentication
│   ├── common/          # shared logic and Excel report processing pipeline
│   ├── reports/         # upload, status tracking, download, and report display
│   ├── schedules/       # weekly schedule management and display
│   ├── settings.py      # project configuration
│   ├── urls.py          # main URL routing
│   └── ...
├── requirements.txt
├── manage.py
├── LICENSE
├── README.md
├── README_BG.md
├── README_EN.md
└── venv/
```

## Why this is useful for a CV

This project is a strong candidate for a Data Analyst / Data Engineer CV because it demonstrates:

- Working with tabular data and Excel formats
- Building a data processing pipeline for uploaded files
- Extracting, transforming, and normalizing data
- Calculating metrics and KPIs
- Generating visual outputs from data
- Applying Python in real analytics tasks
- Combining backend development with data workflow logic

It shows the ability to turn raw data into a structured, analyzed, and reportable format — a core skill in analytics and data engineering.

## Requirements

- Python 3.10+
- pip
- PostgreSQL database
- Cloudinary account
- SMTP email configuration

## Environment variables

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

```bash
git clone https://github.com/Omayski13/Football_schedule.git
cd Football_schedule
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Data workflow description

When a user uploads a report file, the system:

1. accepts the file through a Django view
2. creates temporary input and output directories
3. reads the data using pandas
4. extracts headers, dates, players, and attendance fields
5. processes the presence/absence logic
6. calculates statistics and KPIs
7. generates visual charts
8. saves everything into a ZIP archive for download

This is a clear ETL-style workflow, where raw data is transformed into a structured and analysis-ready output.

## Use cases

This project is suitable for:

- coaches and sports managers
- football clubs and youth academies
- attendance analysis
- day-to-day reporting in sports organizations
- presenting data in a clear and visual format

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Conclusion

Football Schedule combines a sports management context with a practical data workflow. It demonstrates not only schedule management, but also real-world data work: collection, processing, analysis, and visualization.

This makes it especially relevant for roles such as Data Analyst, Data Engineer, and Analytics Engineer.
