from datetime import datetime

class Student:
    def __init__(self, student_id, full_name, date_of_birth):
        self.student_id = student_id
        self.full_name = full_name
        self.date_of_birth = datetime.strptime(date_of_birth, "%d-%m-%Y")

    @property
    def last_name(self):
        return self.full_name.split()[-1]

    @property
    def first_name(self):
        return " ".join(self.full_name.split()[:-1])

    @property
    def age(self):
        today = datetime.today()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def print_information(self):
        return (f"ID: {self.student_id}, {self.full_name}, "
                f"{self.date_of_birth.strftime('%d-%m-%Y')}, Age: {self.age}")


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_total_students(self):
        return len(self.students)

    def find_students_by_name(self, name):
        return [student for student in self.students if name.lower() in student.full_name.lower()]

    def find_students_with_birthday_in_current_month(self):
        current_month = datetime.today().month
        return [student for student in self.students if student.date_of_birth.month == current_month]

    def sort_students_by_age(self):
        self.students.sort(key=lambda student: student.age)
        return self.students

    def sort_students_by_age_desc(self):
        self.students.sort(key=lambda student: student.age, reverse=True)
        return self.students

    def return_array(self):
        return self.students

    def remove_by_id(self, student_id):
        success = False
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                self.students.pop(i)
                success = True
        if not success:
            print("ID not found to delete")
        return self.students

