# Student Management System

### Overview
A desktop GUI application designed to streamline student data management. It replaces traditional records with a highly scalable, schema-less NoSQL database structure, providing a fast and secure administrative interface.

### Technologies Used
* Python (Tkinter for GUI)
* MongoDB (PyMongo)
* Cryptography (SHA-256 hashing)

### Key Features
* **Secure Authentication:** User login passwords are encrypted and stored using SHA-256 hashing.
* **Flexible Database Architecture:** Utilizes MongoDB for horizontal scalability and fast read/writes, allowing the system to adapt to data changes without redesigning schemas.
* **Robust Data Validation:** Implemented checks to handle missing fields, prevent duplicate UIDs, and utilize `try-except` blocks to handle database connection failures smoothly.
