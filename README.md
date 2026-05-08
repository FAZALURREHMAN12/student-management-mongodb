# Student Management System

A desktop-based student management application built with Python, Tkinter, and MongoDB. The system provides a graphical interface for managing student records with secure authentication, CRUD operations, and MongoDB database integration.

## Preview

> Add the screenshots you uploaded into a `screenshots` folder in the repo and keep these names:
>
> - `login-screen.png`
> - `main-menu.png`
> - `add-student.png`
> - `student-details.png`

### Login Screen

![Login Screen](screenshots/login-screen.png)

### Main Dashboard

![Main Menu](screenshots/main-menu.png)

### Add Student Window

![Add Student](screenshots/add-student.png)

### Student Details View

![Student Details](screenshots/student-details.png)

## Overview

This project was designed to simplify student record management through a desktop GUI application connected to a MongoDB database. It replaces traditional file-based record systems with a scalable NoSQL database approach.

The application allows administrators to securely log in and perform operations such as adding, updating, deleting, and viewing student information through an easy-to-use graphical interface.

## Features

- Secure user registration and login system
- Password hashing using SHA-256
- Add, update, delete, and display student records
- MongoDB integration using PyMongo
- GUI built with Python Tkinter
- Input validation and duplicate checking
- Error handling using try-except blocks
- Simple and user-friendly desktop interface

## Tech Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| GUI Framework | Tkinter |
| Database | MongoDB |
| Database Driver | PyMongo |
| Security | SHA-256 hashing |

## System Modules

### Authentication System
- User registration
- Secure login handling
- Password encryption using SHA-256

### Student Record Management
- Add new students
- Update existing student information
- Delete student entries
- Display all stored student records

### Database Layer
- MongoDB collections for storing records
- CRUD operations through PyMongo
- Validation and exception handling

## What this project demonstrates

- Desktop GUI development with Python
- MongoDB database integration
- NoSQL database design concepts
- Secure authentication handling
- CRUD application architecture
- Input validation and error handling

## How to run locally

1. Clone the repository:

```bash
git clone https://github.com/FAZALURREHMAN12/student-management-mongodb.git
```

2. Open the project folder:

```bash
cd student-management-mongodb
```

3. Install dependencies:

```bash
pip install pymongo
```

4. Start MongoDB locally.

5. Run the main Python file:

```bash
python main.py
```

> Note: The entry filename may differ depending on your project structure.

## Future Improvements

- Add role-based access control
- Improve UI styling and responsiveness
- Add search and filtering functionality
- Export records to CSV/PDF
- Add attendance and grading modules
- Deploy database remotely using MongoDB Atlas

## Author

**Fazal Ur Rehman**  
GitHub: [FAZALURREHMAN12](https://github.com/FAZALURREHMAN12)
