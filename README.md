# multi-container_appliication

This project demonstrates how to containerize a multi-tier web application using Docker Compose. The application consists of a frontend service, a backend service, and a database service.

## Prerequisites
Before you begin, ensure you have the following installed:

- Docker: Install Docker
- Docker Compose: Install Docker Compose

## Project Structure
- frontend/: Contains files for the frontend service.
- backend/: Contains files for the backend service.
- docker-compose.yml: Defines the services, networks, and volumes for the application.

## Getting Started

Follow these instructions to get the multi-tier web application up and running using Docker Compose.

### Step 1: Clone the Repository

```
git clone https://github.com/ajayD1345/multi-container_appliication.git
cd multi-container_appliication

### Step 2: Build the Docker Images

sudo docker-compose build

### Step 3: Run the Docker Containers

sudo docker-compose up

### Step 4: Access the Application
Open your web browser and navigate to http://localhost:8080. You should see the frontend page, and it should display the data fetched from the backend service.
```

## Accessing the Application
- Frontend: Access the frontend application at http://localhost:8080.
- Backend: If the backend exposes a web interface, access it at http://localhost:5000/data.

##Troubleshooting
If you encounter any issues with building or running the application, check the logs using 'sudo docker-compose logs' for more information.

# Authur
Hamed Ayojide

