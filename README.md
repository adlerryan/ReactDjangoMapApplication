# Map Application with Django and Google Maps API
This repository contains a web application that integrates React for the frontend and Django for the backend. The main functionality revolves around displaying and managing map-related data.

# Update
- Continuously updating this repository.
- Front-end changes to be addressed.
  
https://github.com/adlerryan/ReactDjangoMapApplication/assets/131544944/180425e7-9910-4790-a1a0-807c0b9c243e

## Front-end (React)
- **frontend:** This directory houses the React frontend of the application.
- **src:** Contains the main React components and logic.
- **App.js:** The main React component.
- **Map.js:** Likely contains the logic and components related to map display and interaction.
- **Header.js:** Represents the header component of the application.
- **public:** Contains static assets like images, HTML templates, and manifest files.
#### Other Files
- **manage.py:** A command-line utility that lets you interact with the Django project in various ways.
- **db.sqlite3:** SQLite database file.
- **spot_images:** Contains images related to the application.

## Backend
- **drycana:** This is the primary Django app. It contains the following key components:

  - **models.py:** Defines the data models used in the application.
  - **views.py:** Contains the logic for handling HTTP requests.
  - **serializers.py:** Used for converting complex data types, such as Django models, into a format that can be easily rendered into JSON, XML, or other content types.
  - **urls.py:** Defines the URL patterns for the app.
  - **admin.py:** Configurations for the Django admin interface.
  - **migrations:** Contains database migration scripts.
  - **page:** Another Django app in the repository. It has similar components as the drycana app, such as models, views, serializers, and URLs.

## Installation and Setup
**Prerequisites:**
Before you begin, ensure you have the following installed:
  - Python (version 3.7 or newer)
  - Node.js and npm
  - Django
  - Django Rest Framework

#### Steps:
**1. Clone the Repository:**
```
git clone https://github.com/adlerryan/ReactDjangoMapApplication.git
```
Navigate to the root directory of the project:
```
cd ReactDjangoMapApplication
```
**2. Set Up the Backend (Django):**

a. Navigate to the root directory of the project:
```
cd ReactDjangoMapApplication
```
b. Create a virtual environment:
```
python -m venv venv
```
c. Activate the virtual environment:

- On Windows:
```
.\venv\Scripts\activate
```
- On macOS and Linux:
```
source venv/bin/activate
```
d. Install the required Python packages:
```
pip install -r requirements.txt
```
e. Run the migrations to set up the database:
```
python manage.py migrate
```
f. Start the Django development server:
```
python manage.py runserver
```
**3. Set Up the Frontend (React):**

a. Navigate to the frontend directory:
```
cd frontend
```
b. Install React and its dependencies (if not already listed in package.json):
```
npm install react react-dom react-scripts
```
c. Install the other required npm packages:
```
npm install
```
**4. Run the Application:**

From the frontend directory, use the following command to start both the backend and frontend:
```
npm run dev
```
**5. Access the Application:**
  - The Django backend should be running at http://localhost:8000/
  - The React frontend should be accessible at http://localhost:3000/
**6. Optional (Django Admin Setup):**
If you wish to access the Django admin interface:
a. Create a superuser:
```
python manage.py createsuperuser
```
b. Access the admin interface at **http://localhost:8000/admin/**
