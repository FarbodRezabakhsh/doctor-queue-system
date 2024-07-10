# Online Doctor Appointment System

This project is an online system for managing and booking doctor appointments by patients. By developing this project, you can help the stakeholders of this community.

## Features

- **Doctor Management:**
    - Admins can add doctors with various specializations.
    - Each admin can specify available times for doctor visits.
    - Set fees for each visit.

- **Doctor Search:**
    - Users can search for doctors by specialization or name.

- **Appointment Booking:**
    - Select visit times from the doctor's available slots.
    - Pay the visit fee through the wallet.
    - Send booking confirmation via email.

- **Reviews and Ratings:**
    - Users can write reviews about the doctors they have visited.
    - Users who have been visited can rate the doctors.

- **Others:**
    - Use Django authentication and OTP system.
    - User registration and login through services like Google and OAuth (optional and includes extra points).
    - Put the project in production mode (includes using production environment web servers, setting relevant configurations in production mode, collecting static files, and so on).
    - Dockerize the project.
    - Use environment variables (`.env` file) for settings dependent on the execution environment such as secret keys, database settings, debug mode, etc.
    - Follow the MVT (Model-View-Template) architecture.
    - Use desired tools for writing tests.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd doctor_appointment_system
Create a virtual environment and activate it:


    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:


    pip install -r requirements.txt
Setup environment variables:
Create a .env file in the root directory of the project and add the necessary environment variables such as:


    SECRET_KEY='your-secret-key'
    DEBUG=True
    DATABASE_URL='sqlite:///db.sqlite3'
Apply migrations:


    python manage.py makemigrations
    python manage.py migrate
Run the development server:


    python manage.py runserver
Create a superuser:


python manage.py createsuperuser
Access the admin site:
Visit http://127.0.0.1:8000/admin to log in as the superuser and manage doctors, specializations, and appointments.

Project Structure

    online_doctor_appointment_system/
    ├── appointments/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── css/
    │   ├── style.css
    │   └── layout.css
    ├── doctors/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── feedback/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── templates/
    │   ├── appointments/
    │   │   ├── appointment_form.html
    │   │   ├── appointment_success.html
    │   ├── doctors/
    │   │   ├── doctor_detail.html
    │   ├── feedback/
    │   │   ├── feedback_form.html
    │   ├── registration/
    │   │   ├── login.html
    │   │   ├── signup.html
    │   │   ├── logged_out.html
    │   │   ├── logout_confirm.html
    │   │   ├── password_reset_form.html
    │   │   ├── password_reset_done.html
    │   │   ├── password_reset_confirm.html
    │   │   ├── password_reset_complete.html
    │   │   ├── acc_active_email.html
    │   ├── users/
    │   │   ├── profile.html
    ├── online_doctor_appointment_system/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py 
    │   └── wsgi.py
    ├── manage.py
    └── README.md


Dockerization
To run the project using Docker:

Build the Docker image:


    docker build -t doctor_appointment_system .
Run the Docker container:


    docker run -p 8000:8000 doctor_appointment_system
Access the application:
Visit http://127.0.0.1:8000 to use the application.

Running Tests
To run the tests, use the following command:


    python manage.py test
Contributing
If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License.