# Task Manager Application

## Overview
Full-stack task management application with Flask backend, HTML/CSS/JS frontend, and MongoDB database.

## Architecture
- **Frontend**: Nginx + HTML/CSS/JavaScript with SDAIA branding
- **Backend**: Flask REST API (Python)
- **Database**: MongoDB

## Docker Images
- `xilv2/aks-backend:latest`
- `xilv2/aks-frontend:latest`

## Kubernetes Resources
- **Namespace**: `task-manager`
- **Frontend**: LoadBalancer service (port 80) - External access
- **Backend**: ClusterIP service (port 5000) - Internal only
- **MongoDB**: ClusterIP service (port 27017) - Internal only

## API Endpoints
- `GET /` - Health check
- `GET /tasks` - Get all tasks
- `POST /tasks` - Create new task (body: {title: "..."})
- `PUT /tasks/<id>` - Update task (body: {title: "..."})
- `DELETE /tasks/<id>` - Delete task

## Features
- SDAIA brand colors (Navy, Teal, Coral)
- Real-time task updates every 5 seconds
- Professional gradient design
- Responsive UI
- Edit and delete tasks
- Smooth animations

## Deployment
Automatically deployed via GitLab CI/CD pipeline when changes are pushed to apps/task-manager/.

## Local Testing
```bash
cd apps/task-manager
docker-compose up
```

Access at: http://localhost:8080
