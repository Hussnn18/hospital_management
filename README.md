# Hospital Management System

A full-stack web application built with Python Flask and MySQL that manages core hospital operations — patients, doctors, appointments, treatments, and billing — through a clean dashboard interface.

## What It Does

The system has 5 modules accessible from a central dashboard:

| Module | What it manages |
|--------|----------------|
| **Patients** | Add, view, and delete patient records (name, age, gender, phone) |
| **Doctors** | Manage doctor details and specializations |
| **Appointments** | Schedule appointments linking patients to doctors with date and disease info |
| **Treatments** | Record treatment descriptions and medicines linked to appointments |
| **Billing** | Generate and track bills linked to patient records |

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| Web Framework | Flask |
| Database | MySQL |
| DB Connector | mysql-connector-python |
| Frontend | HTML, CSS, Bootstrap |
| Templating | Jinja2 |

## Project Structure

```
hospital management/
├── app.py               # Flask app with all routes
├── db.py                # MySQL database connection
├── static/
│   └── style.css        # Custom styling
└── templates/
    ├── base.html        # Base layout template
    ├── dashboard.html   # Main dashboard
    ├── patient.html     # Patient management
    ├── doctor.html      # Doctor management
    ├── appointment.html # Appointment scheduling
    ├── treatment.html   # Treatment records
    └── bill.html        # Billing module
```

## Database Schema

Set up the MySQL database with the following tables:

```sql
CREATE DATABASE mydb;
USE mydb;

CREATE TABLE patient (
    patient_id INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(15)
);

CREATE TABLE doctor (
    doctor_id INT PRIMARY KEY,
    Name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE appointment (
    appointment_id INT PRIMARY KEY,
    appointment_date DATE,
    disease VARCHAR(100),
    patient_id INT,
    doctor_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

CREATE TABLE treatment (
    treatment_id INT PRIMARY KEY,
    description VARCHAR(255),
    medicine VARCHAR(255),
    appointment_id INT,
    FOREIGN KEY (appointment_id) REFERENCES appointment(appointment_id)
);

CREATE TABLE bill (
    bill_id INT PRIMARY KEY,
    amount DECIMAL(10,2),
    bill_date DATE,
    patient_id INT,
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id)
);
```

## How to Run

### Prerequisites
- Python 3.x installed
- MySQL Server installed and running

### Step 1 — Install required libraries

```bash
pip install flask mysql-connector-python
```

### Step 2 — Set up the database

Open MySQL and run the SQL schema above to create the database and tables.

### Step 3 — Update database credentials

Open `db.py` and update with your MySQL username and password:

```python
return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Husan1807",
    database="mydb"
)
```

### Step 4 — Run the app

```bash
python app.py
```

### Step 5 — Open in browser

```
http://127.0.0.1:5000
```

You will see the dashboard with links to all 5 modules.

## Key Concepts Demonstrated

- **Flask routing** — separate route for each module (`/patients`, `/doctors`, `/appointments`, etc.)
- **MySQL JOIN queries** — appointments page joins patient and doctor tables to display names
- **Jinja2 templating** — base template with blocks, data passed from routes to HTML
- **CRUD operations** — add and delete records across all modules
- **Relational database design** — foreign key relationships between tables
- **Separation of concerns** — database connection logic separated into `db.py`

## Project Purpose

Built as a DBMS course project to demonstrate practical database design, relational schema modeling, SQL JOIN queries, and integration of a MySQL backend with a Python Flask web application.

---

*Developed by Husanpreet Singh,Jashan | B.Tech CSE, GNDEC
