# Library Management System 📚

![Project Type](https://img.shields.io/badge/Type-Web%20Application-blue)
![Framework](https://img.shields.io/badge/Framework-Django-green)
![Language](https://img.shields.io/badge/Language-Python-yellow)

## Overview

This **Library Management System** is a web application developed using **Python** and the **Django** framework. Designed to streamline library operations, the system enables both users and administrators to manage book inventories, register and login, issue books, and submit feedback.

The system is composed of **four core Django apps**:

- `useraccounts`: Handles **user registration, login, and logout**, ensuring authentication and authorization.
- `feedback`: Allows users to **submit reviews or feedback** on books they've read.
- `bookapp`: The core of the system — users can **browse, issue, view details, update, or delete books**. Admins have additional privileges for book management.

## Features

- 🔐 **User Authentication**: Secure login, logout, and registration system.
- 📘 **Book Inventory**: Add, update, delete, and view books.
- 🙋 **Feedback System**: Users can leave reviews for books.
- 📄 **Issuance Tracking**: Keep records of which user has which book.
- 🛠️ **Admin Privileges**: Admin users can manage all book data.
- 📂 **Modular Structure**: Organized into independent Django apps for clarity and maintainability.

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Django Templates
- **Database**: SQLite (default Django database)
- **Other**: Bootstrap (optional), Django Admin

## Getting Started

### Prerequisites

- Python 3.x
- Django 2.x or 3.x

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-django.git
   cd library-management-django
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
6. Start the development server:
   ```bash
   python manage.py runserver
7. Access the app:
Open your browser and go to `http://127.0.0.1:8000/`

## Suggested Project Structure
library-management/
- bookapp/           # Book-related operations (CRUD, issue)
- feedback/          # Book reviews and feedback
- useraccounts/      # Authentication system
- library/           # Project settings and URLs
- templates/         # HTML templates
- static/            # CSS, JS, images
- db.sqlite3         # SQLite database
- manage.py          # Django management script

## 📸 Screenshots

### 🔐 Login Page
![Login Page](screenshots/login_page.png)

### 📚 Book List
![Book List](screenshots/book_list.png)

### 📝 Feedback Form
![Feedback Form](screenshots/feedback_form.png)

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Credits
Developed as a self-learning project in 2019 to understand the Django web framework.<br/>
[Connect with me on LinkedIn](https://www.linkedin.com/in/ferrindsouza)
