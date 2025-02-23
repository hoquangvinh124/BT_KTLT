class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.registered_subjects = []

    def __str__(self):
        return f"[Student] ID: {self.student_id}, Name: {self.student_name}, " \
               f"Subjects: {self.registered_subjects}"

class ClassRoom:
    def __init__(self, class_code, class_name):
        self.class_code = class_code
        self.class_name = class_name
        self.students = []
        self.subjects = []

    def __str__(self):
        return f"[ClassRoom] Code: {self.class_code}, Name: {self.class_name}, " \
               f"Students: {self.students}, Subjects: {self.subjects}"


class Subject:
    def __init__(self, subject_code, subject_name, credit, belongs_to_class_code):
        self.subject_code = subject_code
        self.subject_name = subject_name
        self.credit = credit
        self.belongs_to_class_code = belongs_to_class_code

    def __str__(self):
        return f"[Subject] Code: {self.subject_code}, Name: {self.subject_name}, " \
               f"Credit: {self.credit}, Class: {self.belongs_to_class_code}"
