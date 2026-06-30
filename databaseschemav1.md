# Database Schema

## Overview

A simple database design for a team portfolio website where clients can:

* View team members
* View services
* View projects
* Contact the team

---

## TeamMember

Stores information about team members.

| Field         | Type         |
| ------------- | ------------ |
| id            | pk       |
| full_name     | VARCHAR(100) |
| role          | VARCHAR(100) |
| bio           | TEXT         |
| email         | VARCHAR(255) |
| phone         | VARCHAR(50)  |
| profile_image | VARCHAR(255) |
| skills        | JSON/TEXT    |
| github_url    | VARCHAR(255) |
| linkedin_url  | VARCHAR(255) |

Example skills:

```json
["Python", "Django", "React", "Flutter"]
```

---

## Service

Stores services offered by the team.

| Field       | Type         |
| ----------- | ------------ |
| id          | pk           |
| title       | VARCHAR(200) |
| description | TEXT         |
| icon        | VARCHAR(255) |

Examples:

* Website Development
* Mobile App Development
* API Development
* Cybersecurity Services

---

## Project

Stores portfolio projects.

| Field        | Type         |
| ------------ | ------------ |
| id           | BIGINT       |
| title        | VARCHAR(255) |
| description  | TEXT         |
| technologies | JSON/TEXT    |
| thumbnail    | VARCHAR(255) |
| project_url  | VARCHAR(255) |
| github_url   | VARCHAR(255) |

Example technologies:

```json
["Django", "React", "MySQL"]
```

---

## Inquiry

Stores contact messages and quote requests.

| Field      | Type          |
| ---------- | ------------- |
| id         | BIGINT        |
| name       | VARCHAR(100)  |
| email      | VARCHAR(255)  |
| phone      | VARCHAR(50)   |
| service    | VARCHAR(100)  |
| budget     | DECIMAL(10,2) |
| message    | TEXT          |
| created_at | DATETIME      |

---

## User

Django built-in authentication table.

Used for:

* Admin login
* Managing team members
* Managing services
* Managing projects
* Viewing client inquiries

---

## Final Tables

1. TeamMember
2. Service
3. Project
4. Inquiry
5. User (Django Built-in)
