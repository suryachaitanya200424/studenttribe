# Appointment Management System

A simple **Python-based Appointment Management System** that allows users to **book, view, update, and delete appointments** through a command-line interface (CLI). This project demonstrates the use of **Object-Oriented Programming (OOP)** concepts such as classes, objects, instance methods, class methods, and class variables.

## Features

* Book a new appointment
* View all appointments
* Update an existing appointment
* Delete an appointment
* Menu-driven command-line interface
* Stores appointment data during program execution

## Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Command-Line Interface (CLI)

## Project Structure

```text
Appointment-Management-System/
│
├── appointment.py     # Main Python program
└── README.md          # Project documentation
```

## How It Works

Each appointment stores:

* Patient Name
* Doctor Name
* Appointment Date
* Appointment Time

The program maintains a list of appointments and provides options to manage them using a simple menu.

## Menu Options

```text
===== Appointment Menu Management =====
1. Book Your Appointment
2. View Your Appointments
3. Update Appointment
4. Delete Appointment
5. Exit
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Appointment-Management-System.git
```

2. Navigate to the project folder:

```bash
cd Appointment-Management-System
```

3. Run the program:

```bash
python appointment.py
```

## Sample Output

```text
===== Appointment Menu Management =====
1. Book Your Appointment
2. View Your Appointments
3. Update Appointment
4. Delete Appointment
5. Exit

Enter your choice: 1

Enter patient name: Surya
Enter doctor name: Dr. Rao
Enter date (DD-MM-YYYY): 15-08-2026
Enter time (HH:MM): 10:30

Appointment booked successfully!
```

Viewing appointments:

```text
===== APPOINTMENT DETAILS =====
Appointment Number: 1
Patient : Surya
Doctor  : Dr. Rao
Date    : 15-08-2026
Time    : 10:30
------------------------------
```

## OOP Concepts Used

* **Class** – `Appointment`
* **Object Creation** – Creating appointment objects
* **Instance Methods** – `display()`
* **Class Methods** – `view_appointments()`, `update_appointment()`, `delete_appointment()`
* **Class Variable** – `appointments`

## Future Improvements

* Save appointments permanently using a database (SQLite/MySQL/PostgreSQL)
* Search appointments by patient or doctor name
* Add appointment validation (date and time checking)
* Build a graphical user interface (GUI) using Tkinter or PyQt
* Develop a web version using Flask or Django

## Author

**Surya Chaitanya**

If you found this project useful, consider giving it a **star** on GitHub.
