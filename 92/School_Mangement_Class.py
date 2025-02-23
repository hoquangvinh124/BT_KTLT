from Class_Student_Subject_Class import *
from Section_Class import *
from FileUtil import FileUtil

class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.classes = {}
        self.subjects = {}
        self.sections = {}

    #STUDENT Methods
    def add_student(self):
        student_id = input("Nhập Student ID: ")
        if student_id in self.students:
            print("Student ID đã tồn tại!")
            return
        student_name = input("Nhập Student Name: ")
        student = Student(student_id, student_name)
        self.students[student_id] = student
        print("Thêm student thành công!")

    def edit_student(self):
        student_id = input("Nhập Student ID cần sửa: ")
        if student_id not in self.students:
            print("Student ID không tồn tại!")
            return
        new_name = input("Nhập tên mới cho student: ")
        self.students[student_id].student_name = new_name
        print("Sửa student thành công!")

    def delete_student(self):
        student_id = input("Nhập Student ID cần xóa: ")
        if student_id not in self.students:
            print("Student ID không tồn tại!")
            return
        for cls in self.classes.values():
            if student_id in cls.students:
                cls.students.remove(student_id)
        del self.students[student_id]
        print("Xóa student thành công!")

    #CLASS Methods
    def add_class(self):
        class_code = input("Nhập Class Code: ")
        if class_code in self.classes:
            print("Class Code đã tồn tại!")
            return
        class_name = input("Nhập Class Name: ")
        classroom = ClassRoom(class_code, class_name)
        self.classes[class_code] = classroom
        print("Thêm class thành công!")

    def edit_class(self):
        class_code = input("Nhập Class Code cần sửa: ")
        if class_code not in self.classes:
            print("Class Code không tồn tại!")
            return
        new_class_name = input("Nhập tên lớp mới: ")
        new_teacher_name = input("Nhập tên giảng viên mới: ")
        c = self.classes[class_code]
        c.class_name = new_class_name
        c.teacher_name = new_teacher_name
        print("Sửa class thành công!")

    def delete_class(self):
        class_code = input("Nhập Class Code cần xóa: ")
        if class_code not in self.classes:
            print("Class Code không tồn tại!")
            return
        to_delete_subjects = []
        for subj_code, subj_obj in self.subjects.items():
            if subj_obj.belongs_to_class_code == class_code:
                to_delete_subjects.append(subj_code)
        for s in to_delete_subjects:
            del self.subjects[s]
        del self.classes[class_code]
        print("Xóa class thành công!")

    #SUBJECT Methods
    def add_subject(self):
        subject_code = input("Nhập Subject Code: ")
        if subject_code in self.subjects:
            print("Subject Code đã tồn tại!")
            return
        subject_name = input("Nhập Subject Name: ")
        credit = int(input("Nhập số tín chỉ: "))
        belongs_to_class_code = input("Nhập Class Code (môn này thuộc lớp nào?): ")
        if belongs_to_class_code not in self.classes:
            print("Class Code không tồn tại! Hãy thêm lớp trước.")
            return
        subj = Subject(subject_code, subject_name, credit, belongs_to_class_code)
        self.subjects[subject_code] = subj
        self.classes[belongs_to_class_code].subjects.append(subject_code)
        print("Thêm subject thành công!")

    def edit_subject(self):
        subject_code = input("Nhập Subject Code cần sửa: ")
        if subject_code not in self.subjects:
            print("Subject Code không tồn tại!")
            return
        new_name = input("Nhập tên môn học mới: ")
        new_credit = int(input("Nhập số tín chỉ mới: "))
        self.subjects[subject_code].subject_name = new_name
        self.subjects[subject_code].credit = new_credit
        print("Sửa subject thành công!")

    def delete_subject(self):
        subject_code = input("Nhập Subject Code cần xóa: ")
        if subject_code not in self.subjects:
            print("Subject Code không tồn tại!")
            return
        subj = self.subjects[subject_code]
        class_code = subj.belongs_to_class_code
        if class_code in self.classes:
            if subject_code in self.classes[class_code].subjects:
                self.classes[class_code].subjects.remove(subject_code)
        del self.subjects[subject_code]
        print("Xóa subject thành công!")

    #SECTION Methods
    def add_section(self):
        section_code = input("Nhập Section Code: ")
        if section_code in self.sections:
            print("Section Code đã tồn tại!")
            return
        subject_code = input("Nhập Subject Code: ")
        course_code = input("Nhập Course Code: ")
        num_credits = int(input("Nhập số tín chỉ: "))
        start_date = input("Nhập start date: ")
        end_date = input("Nhập end date: ")

        sec = Section(section_code, subject_code, course_code, num_credits, start_date, end_date)
        self.sections[section_code] = sec
        print("Thêm section thành công!")

    #REGISTRATION Methods
    def register_student_to_subject(self):
        student_id = input("Nhập Student ID cần đăng ký môn học: ")
        if student_id not in self.students:
            print("Student ID không tồn tại!")
            return
        subject_code = input("Nhập Subject Code muốn đăng ký: ")
        if subject_code not in self.subjects:
            print("Subject Code không tồn tại!")
            return
        if subject_code not in self.students[student_id].registered_subjects:
            self.students[student_id].registered_subjects.append(subject_code)
            class_code = self.subjects[subject_code].belongs_to_class_code
            if student_id not in self.classes[class_code].students:
                self.classes[class_code].students.append(student_id)
            print("Đăng ký môn học thành công!")
        else:
            print("Sinh viên đã đăng ký môn này rồi!")

    def unregister_student_from_subject(self):
        student_id = input("Nhập Student ID cần hủy đăng ký: ")
        if student_id not in self.students:
            print("Student ID không tồn tại!")
            return
        subject_code = input("Nhập Subject Code muốn hủy: ")
        if subject_code in self.students[student_id].registered_subjects:
            self.students[student_id].registered_subjects.remove(subject_code)
            print("Hủy đăng ký môn học thành công!")
        else:
            print("Sinh viên chưa đăng ký môn này!")

    #VIEW Methods
    def view_class_list_with_teacher(self):
        if not self.classes:
            print("Chưa có lớp nào!")
            return
        print("=== Danh sách Class ===")
        for c in self.classes.values():
            print(f"ClassCode: {c.class_code}, ClassName: {c.class_name}")

    def view_class_list_for_each_registered_course(self):
        if not self.subjects:
            print("Chưa có môn học nào!")
            return
        print("=== Danh sách môn học và lớp tương ứng ===")
        for s in self.subjects.values():
            print(f"SubjectCode: {s.subject_code}, Name: {s.subject_name}, "
                  f"BelongsToClass: {s.belongs_to_class_code}")

    def view_courses_for_each_registered_class(self):
        if not self.classes:
            print("Chưa có lớp nào!")
            return
        print("=== Danh sách môn học cho mỗi lớp ===")
        for c in self.classes.values():
            print(f"\nClassCode: {c.class_code}, ClassName: {c.class_name}")
            if not c.subjects:
                print("  -> Chưa có môn học nào.")
            else:
                for subj_code in c.subjects:
                    subj_obj = self.subjects[subj_code]
                    print(f"  - SubjectCode: {subj_obj.subject_code}, Name: {subj_obj.subject_name}")

    #LOAD/SAVE Methods
    def save_data(self, filename="database.pkl"):
        success = FileUtil.savemodel(self, filename)
        if success:
            print("Đã lưu dữ liệu thành công vào file:", filename)
        else:
            print("Lưu dữ liệu thất bại.")

    def load_data(self, filename="database.pkl"):
        obj = FileUtil.loadmodel(filename)
        if obj is not None:
            self.students = obj.students
            self.classes = obj.classes
            self.subjects = obj.subjects
            self.sections = obj.sections
            print("Đã đọc dữ liệu thành công từ file:", filename)
        else:
            print("Không thể đọc dữ liệu từ file:", filename)