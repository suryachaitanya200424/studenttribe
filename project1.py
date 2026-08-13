class Appointment:
    appointments = []

    def __init__(self, patient_name, doctor_name, date, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time

    def display(self):
        print("Patient :", self.patient_name)
        print("Doctor  :", self.doctor_name)
        print("Date    :", self.date)
        print("Time    :", self.time)
        print("-" * 30)

    @classmethod
    def view_appointments(cls):
        if len(cls.appointments) == 0:
            print("No appointments found.")
        else:
            print("\n===== APPOINTMENT DETAILS =====")
            for index, appt in enumerate(cls.appointments, start=1):
                print("Appointment Number:", index)
                appt.display()

    @classmethod
    def update_appointment(cls):
        if len(cls.appointments) == 0:
            print("No appointments available to update.")
            return

        cls.view_appointments()

        num = int(input("Enter appointment number to update: "))

        if 1 <= num <= len(cls.appointments):
            appt = cls.appointments[num - 1]

            appt.patient_name = input("Enter new patient name: ")
            appt.doctor_name = input("Enter new doctor name: ")
            appt.date = input("Enter new date (DD-MM-YYYY): ")
            appt.time = input("Enter new time (HH:MM): ")

            print("Appointment updated successfully!")
        else:
            print("Invalid appointment number.")

    @classmethod
    def delete_appointment(cls):
        if len(cls.appointments) == 0:
            print("No appointments available to delete.")
            return

        cls.view_appointments()

        num = int(input("Enter appointment number to delete: "))

        if 1 <= num <= len(cls.appointments):
            cls.appointments.pop(num - 1)
            print("Appointment deleted successfully!")
        else:
            print("Invalid appointment number.")


# -------------------- MENU --------------------

while True:
    print("\n===== Appointment Menu Management =====")
    print("1. Book Your Appointment")
    print("2. View Your Appointments")
    print("3. Update  Appointment")
    print("4. Delete Appointment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient = input("Enter patient name: ")
        doctor = input("Enter doctor name: ")
        date = input("Enter date (DD-MM-YYYY): ")
        time = input("Enter time (HH:MM): ")

        obj = Appointment(patient, doctor, date, time)
        Appointment.appointments.append(obj)

        print("Appointment booked successfully!")

    elif choice == "2":
        Appointment.view_appointments()

    elif choice == "3":
        Appointment.update_appointment()

    elif choice == "4":
        Appointment.delete_appointment()

    elif choice == "5":
        print("Exiting Appointment Management System...")
        break

    else:
        print("Invalid choice. Please try again.")