from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
from PIL import Image, ImageTk
import hashlib

# --- MongoDB Connection ---
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["student_management"]
    print("Connected to MongoDB")
except Exception as e:
    print("Database connection Error:", e)
    messagebox.showerror("Error", "Database Connection Error")
    exit(1)

# --- Hash Password ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Root Window for Login ---
login_root = Tk()
login_root.geometry("600x450")
login_root.title("Login - Student Management System")
login_root.configure(bg="#ecf0f1")

# --- Login Page UI ---
Label(login_root, text="Welcome to", font=("Arial", 24), fg="#2c3e50", bg="#ecf0f1").pack(pady=(40, 5))
Label(login_root, text="Student Management System", font=("Arial", 28, "bold"), fg="#2c3e50", bg="#ecf0f1").pack(pady=(0, 30))

frame = Frame(login_root, bg="#ecf0f1")
frame.pack(pady=10)

Label(frame, text="Username:", font=("Arial", 18), bg="#ecf0f1").grid(row=0, column=0, pady=15, padx=10, sticky=E)
username_entry = Entry(frame, font=("Arial", 18), width=22)
username_entry.grid(row=0, column=1, pady=15)

Label(frame, text="Password:", font=("Arial", 18), bg="#ecf0f1").grid(row=1, column=0, pady=15, padx=10, sticky=E)
password_entry = Entry(frame, font=("Arial", 18), width=22, show="*")
password_entry.grid(row=1, column=1, pady=15)

# --- Login and Signup Handlers ---
def do_login():
    username = username_entry.get()
    password = password_entry.get()

    if not (username and password):
        messagebox.showwarning("Warning", "Please enter both fields")
        return

    user = db.users.find_one({"username": username})
    if user and user["password"] == hash_password(password):
        messagebox.showinfo("Success", "Login Successful")
        login_root.destroy()
        load_main_app()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

def do_signup():
    username = username_entry.get()
    password = password_entry.get()

    if not (username and password):
        messagebox.showwarning("Warning", "Please enter both fields")
        return

    if db.users.find_one({"username": username}):
        messagebox.showwarning("Warning", "Username already exists")
    else:
        db.users.insert_one({"username": username, "password": hash_password(password)})
        messagebox.showinfo("Success", "User Registered Successfully")

# --- Buttons ---
btn_frame = Frame(login_root, bg="#ecf0f1")
btn_frame.pack(pady=30)

Button(btn_frame, text="Login", command=do_login, font=("Arial", 16, "bold"), bg="#27ae60", fg="white", width=14, height=2).grid(row=0, column=0, padx=15)
Button(btn_frame, text="Sign Up", command=do_signup, font=("Arial", 16, "bold"), bg="#2980b9", fg="white", width=14, height=2).grid(row=0, column=1, padx=15)

# --- Function to Load Main App ---
def load_main_app():
    root = Tk()
    root.geometry("800x600")
    root.title("Student Management System")
    root.configure(bg="#f0f0f0")
    
    
        # Background Image
    bg_img = Image.open("background.png")
    bg_img = bg_img.resize((1300, 820))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(relwidth=1, relheight=1)


    # --- Heading with Logo ---
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((64, 64))
    logo_photo = ImageTk.PhotoImage(logo_img)

    title_frame = Frame(root, bg="#f0f0f0")
    title_frame.pack(pady=20)

    logo_label = Label(title_frame, image=logo_photo, bg="#f0f0f0")
    logo_label.image = logo_photo
    logo_label.pack(side=LEFT, padx=10)

    heading_label = Label(
        title_frame,
        text="Student Management System",
        font=("Arial", 28, "bold"),
        fg="#2c3e50",
        bg="#f0f0f0"
    )
    heading_label.pack(side=LEFT)

    button_style = {
        "font": ("Arial", 16),
        "bg": "#3498db",
        "fg": "white",
        "width": 25,
        "height": 2,
        "bd": 0,
        "activebackground": "#2980b9"
    }

  # Button Functions
    def add_student():
        def add_query():
            uid = uid_entry.get()
            name = name_entry.get()
            email = email_entry.get()
            batch = batch_entry.get()
            mobile = mobile_entry.get()

            if not (uid and name and email and batch):
                messagebox.showwarning("Warning", "All fields are compulsory (except Mobile)")
                return

            student = {'UID': uid, 'NAME': name, 'EMAIL': email, 'BATCH': batch, 'MOBILE': mobile}

            if db.students.count_documents({'UID': uid}, limit=1) == 0:
                db.students.insert_one(student)
                messagebox.showinfo("Success", "Student Added Successfully")
                new_win.destroy()
            else:
                messagebox.showwarning("Error", "Student with this UID already exists")

        new_win = Toplevel(root)
        new_win.geometry("400x400")
        new_win.title("Add Student")

        labels = ["UID", "Name", "Email", "Batch", "Mobile"]
        entries = {}

        for idx, label in enumerate(labels):
            Label(new_win, text=label, font=("Arial", 14)).place(x=20, y=30 + idx*50)
            entry = Entry(new_win, font=("Arial", 14), width=25)
            entry.place(x=120, y=30 + idx*50)
            entries[label.lower()] = entry

        uid_entry = entries["uid"]
        name_entry = entries["name"]
        email_entry = entries["email"]
        batch_entry = entries["batch"]
        mobile_entry = entries["mobile"]

        Button(new_win, text="Submit", command=add_query, font=("Arial", 14), bg="#2ecc71", fg="white").place(x=150, y=320)

    def delete_student():
        def delete():
            uid = uid_entry.get()
            if not uid:
                messagebox.showwarning("Warning", "Enter a UID")
                return

            if db.students.count_documents({'UID': uid}, limit=1) == 0:
                messagebox.showwarning("Error", "Student Not Found")
            else:
                db.students.delete_one({'UID': uid})
                messagebox.showinfo("Success", "Student Deleted")
                new_win.destroy()

        new_win = Toplevel(root)
        new_win.geometry("400x200")
        new_win.title("Delete Student")

        Label(new_win, text="Enter UID:", font=("Arial", 14)).place(x=30, y=50)
        uid_entry = Entry(new_win, font=("Arial", 14), width=25)
        uid_entry.place(x=150, y=50)

        Button(new_win, text="Delete", command=delete, font=("Arial", 14), bg="#e74c3c", fg="white").place(x=150, y=110)

    def update_student():
        def update():
            uid = uid_entry.get()
            if not uid:
                messagebox.showwarning("Warning", "Enter UID to update")
                return

            updates = {}
            if name_entry.get(): updates['NAME'] = name_entry.get()
            if email_entry.get(): updates['EMAIL'] = email_entry.get()
            if batch_entry.get(): updates['BATCH'] = batch_entry.get()
            if mobile_entry.get(): updates['MOBILE'] = mobile_entry.get()

            if not updates:
                messagebox.showwarning("Warning", "Enter at least one field to update")
                return

            if db.students.count_documents({'UID': uid}, limit=1) == 0:
                messagebox.showwarning("Error", "Student Not Found")
            else:
                db.students.update_one({"UID": uid}, {"$set": updates})
                messagebox.showinfo("Success", "Student Updated")
                new_win.destroy()

        new_win = Toplevel(root)
        new_win.geometry("400x400")
        new_win.title("Update Student")

        labels = ["UID", "Name", "Email", "Batch", "Mobile"]
        entries = {}

        for idx, label in enumerate(labels):
            Label(new_win, text=label, font=("Arial", 14)).place(x=20, y=30 + idx*50)
            entry = Entry(new_win, font=("Arial", 14), width=25)
            entry.place(x=120, y=30 + idx*50)
            entries[label.lower()] = entry

        uid_entry = entries["uid"]
        name_entry = entries["name"]
        email_entry = entries["email"]
        batch_entry = entries["batch"]
        mobile_entry = entries["mobile"]

        Button(new_win, text="Update", command=update, font=("Arial", 14), bg="#f39c12", fg="white").place(x=150, y=320)

    def display_students():
        new_win = Toplevel(root)
        new_win.geometry("800x400")
        new_win.title("Student Details")

        headings = ["UID", "Name", "Email", "Batch", "Mobile"]
        for i, h in enumerate(headings):
            Label(new_win, text=h, font=("Arial", 12, "bold"), bg="#bdc3c7", padx=5).grid(row=0, column=i)

        for i, student in enumerate(db.students.find(), start=1):
            Label(new_win, text=student.get("UID", "N/A")).grid(row=i, column=0)
            Label(new_win, text=student.get("NAME", "N/A")).grid(row=i, column=1)
            Label(new_win, text=student.get("EMAIL", "N/A")).grid(row=i, column=2)
            Label(new_win, text=student.get("BATCH", "N/A")).grid(row=i, column=3)
            Label(new_win, text=student.get("MOBILE", "N/A")).grid(row=i, column=4)


    button_frame = Frame(root, bg="#f0f0f0")
    button_frame.pack(pady=30)

    Button(button_frame, text="Add New Student", command=add_student, **button_style).pack(pady=10)
    Button(button_frame, text="Delete Student Entry", command=delete_student, **button_style).pack(pady=10)
    Button(button_frame, text="Update Student Info", command=update_student, **button_style).pack(pady=10)
    Button(button_frame, text="Show Student Details", command=display_students, **button_style).pack(pady=10)

    root.mainloop()

login_root.mainloop()
