# devsiterequest

# Tech Team Portfolio Website

## Project Overview

The Tech Team Portfolio Website is a platform designed to showcase the skills, services, and projects of a team of technology professionals.

The website allows potential clients to:

* Learn about team members
* View technical skills and expertise
* Explore completed projects
* Discover available services
* Contact the team for inquiries
* Request quotations for projects

The goal of the project is to establish an online presence for the team and provide an easy way for clients to connect with us for software development and technology-related services.

---

## Objectives

* Showcase team members and their expertise
* Display services offered by the team
* Present completed projects and portfolio work
* Enable clients to contact the team
* Enable clients to request project quotations
* Provide an administration dashboard for managing website content

---

## Features

### Public Features

* Home Page
* About Us Page
* Team Members Page
* Services Page
* Projects Portfolio Page
* Contact Page
* Quote Request Form

### Admin Features

* Manage Team Members
* Manage Services
* Manage Projects
* View Client Inquiries
* Secure Authentication using JWT

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

### Backend

* Django
* Django REST Framework
* Simple JWT

### Database

* MySQL

### Version Control

* Git
* GitHub

---

## Project Structure

```text
team_portfolio/
│
├── portfolio/        ← Single app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── team_portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── requirements.txt
└── README.md
├── ── apidocumentationv1.md
│   └── databaseschemav1.md
│


```

---

## Database Tables

The application uses the following tables:

1. TeamMember
2. Service
3. Project
4. Inquiry
5. User (Django Authentication)

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/your-username/team-portfolio.git
```

```bash
cd team-portfolio
```

---

### Create Virtual Environment

Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Database

Create a MySQL database.

```sql
CREATE DATABASE team_portfolio;
```

Update database settings in:

```python
settings.py
```

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "team_portfolio",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

---

### Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

---

### Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## API Documentation

The complete API documentation is available in:

```text
docs/api-specification.md
```

---

## Database Documentation

The complete database design is available in:

```text
docs/database-schema.md
```

---

## Future Improvements

* Client Testimonials
* Blog System
* Project Categories
* Project Search
* Email Notifications
* Analytics Dashboard
* Live Chat Integration

---

## Team

This project is developed and maintained by a team of technology professionals specializing in:

* Web Development
* Backend Development
* Mobile Development
* API Development
* Cybersecurity

---

## License

This project is licensed under the MIT License.

```
```
