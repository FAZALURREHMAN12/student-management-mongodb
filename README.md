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

<img width="1282" height="665" alt="Screenshot 2026-05-08 161309" src="https://github.com/user-attachments/assets/42b78f76-3f3f-4842-81fa-c2b096fc051e" />


### Main Dashboard

<img width="1276" height="661" alt="Screenshot 2026-05-08 161459" src="https://github.com/user-attachments/assets/51a56a59-d7af-4b92-83ba-c7aefe3b48d5" />


### Add Student Window

<img width="1275" height="674" alt="Screenshot 2026-05-08 161616" src="https://github.com/user-attachments/assets/b6efae41-2523-4cab-8beb-82e89df17d00" />


### Student Details View

<img width="1278" height="669" alt="Screenshot 2026-05-08 161721" src="https://github.com/user-attachments/assets/58d247ef-f9ab-4103-866b-7e936f8d4cc0" />


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
