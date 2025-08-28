# 🏫 Student Management System (Python)

A simple **Student Management System** built with **Python**.
It allows managing student records (ID, Name, Age, Courses) using a **console-based menu** (and optionally a Tkinter GUI, if added later).
Data is saved to a local file (`students.txt`) so it **persists between sessions**.

---

## 🚀 Features

* 🔑 Login & Registration system (stored in `users.txt`).
* ➕ Add a new student (ID, Name, Age, Courses).
* 👀 View all students.
* 🔍 Search student by ID (and can be extended to search by name).
* ✏️ Update student information (add/remove courses).
* ❌ Delete a student.
* 💾 Save & load data automatically (File Handling).
* 📊 Show number of students per course.
* 📝 Prevent duplicate courses using **sets**.
* 📤 Export student data to CSV (planned feature).
* 🖥️ Console Menu (Tkinter GUI can be added as an extension).

---

## 🛠 Technologies Used

* **Python 3.10+**
* `ast` → Safe file parsing for saving/loading data.
* `csv` → Exporting data (optional).
* `tkinter` → (Optional GUI support).

---

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. Run the program (console version):

   ```bash
   python student_management.py
   ```

3. Login/Register when prompted.

4. Use the menu options:

   ```
   1. Add Student
   2. View Students
   3. Search Student
   4. Update Student
   5. Delete Student
   6. Students per Course
   7. Save & Exit
   ```

---

## 📂 File Structure

```
student-management-system/
│── student_management.py   # Main script
│── students.txt            # Stores student data
│── users.txt               # Stores user login info
│── README.md               # Project documentation
```

---

## ✅ Example Run

```
LOGIN SYSTEM
1. Login  2. Register
Enter choice: 2
Choose a username: admin
Choose a password: 1234
User registered successfully ✅

Welcome to the Student Management System

Enter your choice:
 1. Add Student 
 2. View Students 
 3. Search Student 
 4. Update Student 
 5. Delete Student 
 6. Students per Course 
 7. Save & Exit
