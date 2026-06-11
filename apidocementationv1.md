# API Specification

## Overview

This API powers a simple team portfolio website where clients can:

* View team members
* View services
* View projects
* Submit inquiries
* Administrators can manage website content

Base URL:

```http
/api/
```

---

# Team Members

## Get All Team Members

```http
GET /api/team/
```

Description:

Returns all team members.

---

## Get Team Member Details

```http
GET /api/team/{id}/
```

Description:

Returns a specific team member.

---

# Services

## Get All Services

```http
GET /api/services/
```

Description:

Returns all services offered by the team.

---

## Get Service Details

```http
GET /api/services/{id}/
```

Description:

Returns details of a specific service.

---

# Projects

## Get All Projects

```http
GET /api/projects/
```

Description:

Returns all portfolio projects.

---

## Get Project Details

```http
GET /api/projects/{id}/
```

Description:

Returns details of a specific project.

---

# Client Inquiries

## Submit Inquiry

```http
POST /api/inquiries/
```

Description:

Allows clients to contact the team or request a quote.

Request Body:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+254700000000",
  "service": "Website Development",
  "budget": 500,
  "message": "I need a company website."
}
```

Response:

```json
{
  "message": "Inquiry submitted successfully"
}
```

---

# Admin Authentication

## Login

```http
POST /api/auth/login/
```

Description:

Authenticate administrator.

Request Body:

```json
{
  "username": "admin",
  "password": "password"
}
```

Response:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

# Admin Dashboard APIs

These endpoints require authentication.

---

## Create Team Member

```http
POST /api/team/
```

---

## Update Team Member

```http
PUT /api/team/{id}/
```

---

## Delete Team Member

```http
DELETE /api/team/{id}/
```

---

## Create Service

```http
POST /api/services/
```

---

## Update Service

```http
PUT /api/services/{id}/
```

---

## Delete Service

```http
DELETE /api/services/{id}/
```

---

## Create Project

```http
POST /api/projects/
```

---

## Update Project

```http
PUT /api/projects/{id}/
```

---

## Delete Project

```http
DELETE /api/projects/{id}/
```

---

## View All Inquiries

```http
GET /api/inquiries/
```

Description:

Returns all client inquiries.

---

## Delete Inquiry

```http
DELETE /api/inquiries/{id}/
```

Description:

Deletes an inquiry after it has been handled.

---

# Summary

Public Endpoints:

```http
GET  /api/team/
GET  /api/team/{id}/

GET  /api/services/
GET  /api/services/{id}/

GET  /api/projects/
GET  /api/projects/{id}/

POST /api/inquiries/

POST /api/auth/login/
```

Admin Endpoints:

```http
POST   /api/team/
PUT    /api/team/{id}/
DELETE /api/team/{id}/

POST   /api/services/
PUT    /api/services/{id}/
DELETE /api/services/{id}/

POST   /api/projects/
PUT    /api/projects/{id}/
DELETE /api/projects/{id}/

GET    /api/inquiries/
DELETE /api/inquiries/{id}/
```
