class Patient:
    def __init__(self, name, age, illness):
        self.name = name
        self.age = age
        self.illness = illness
        self.doctor_assigned = None

    def assign_doctor(self, doctor):
        self.doctor_assigned = doctor
        doctor.patients_assigned.append(self)

    def __str__(self):
        doctor_name = self.doctor_assigned.name if self.doctor_assigned else "None"
        return f"Patient: {self.name}, Age: {self.age}, Illness: {self.illness}, Doctor: {doctor_name}"


class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients_assigned = []

    def __str__(self):
        return f"Doctor: {self.name}, Specialty: {self.specialty}, Patients: {[p.name for p in self.patients_assigned]}"


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient_name):
        self.patients = [p for p in self.patients if p.name != patient_name]

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def remove_doctor(self, doctor_name):
        self.doctors = [d for d in self.doctors if d.name != doctor_name]

    def assign_doctor_to_patient(self, doctor_name, patient_name):
        doctor = None
        for d in self.doctors:
            if d.name == doctor_name:
                doctor = d
                break

        patient = None
        for p in self.patients:
            if p.name == patient_name:
                patient = p
                break

        if doctor and patient:
            patient.assign_doctor(doctor)
            return f"Doctor {doctor.name} assigned to Patient {patient.name}"
        return "Doctor or Patient not found"

    def display_patients(self):
        for patient in self.patients:
            print(patient)

    def display_doctors(self):
        for doctor in self.doctors:
            print(doctor)



hospital = Hospital()

doctor1 = Doctor("Doctor Strange", "Time Stop")
doctor2 = Doctor("Spider Man", "Flexibility")

patient1 = Patient("Vinh", 20, "Miss you")
patient2 = Patient("Some random guy", 25, "Michelin guy")

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)
hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.assign_doctor_to_patient("Doctor Strange", "Vinh")
hospital.assign_doctor_to_patient("Spider Man", "Some random guy")


print("\n--- Hospital Patients ---")
hospital.display_patients()

print("\n--- Hospital Doctors ---")
hospital.display_doctors()
