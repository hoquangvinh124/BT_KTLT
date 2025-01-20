from create_class import Student, Address

students = []

def add_student(student):
    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students in the list.")
    else:
        for idx, student in enumerate(students, start=1):
            print(f"{idx}. {student}")

def edit_student(index, first_name=None, last_name=None, home_address=None, school_address=None):
    if 0 <= index < len(students):
        student = students[index]
        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if home_address:
            student.home_address = home_address
        if school_address:
            student.school_address = school_address
        print("Student updated successfully!")
    else:
        print("Invalid student index!")

def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
        print("Student deleted successfully!")
    else:
        print("Invalid student index!")

def filter_students_by_address(address_type, address_value):
    if address_type not in ["home", "school"]:
        print("Invalid address type. Use 'home' or 'school'.")
        return

    filtered_students = [
        student for student in students
        if (student.home_address if address_type == "home" else student.school_address).city == address_value
    ]
    if not filtered_students:
        print("No students found with the given address.")
    else:
        for student in filtered_students:
            print(student)

#Data mau
home_address_1 = Address("Phuc Dat Tower", "Thu Duc", "VN", 12345)
school_address_1 = Address("UEL", "Thu Duc", "VN", 67890)
student_1 = Student("Ho Quang", "Vinh", home_address_1, school_address_1)

home_address_2 = Address("Bcon", "Binh Duong", "VN", 11223)
school_address_2 = Address("Bach Khoa", "Khu Do Thi DHQG", "VN", 44556)
student_2 = Student("Hieu", "Thu Hai", home_address_2, school_address_2)

add_student(student_1)
add_student(student_2)

def input_student():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    print("\nEnter home address:")
    street_address = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter zip code: "))
    home_address = Address(street_address, city, state, zip_code)

    print("\nEnter school address:")
    street_address = input("Enter street address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = int(input("Enter zip code: "))
    school_address = Address(street_address, city, state, zip_code)

    return Student(first_name, last_name, home_address, school_address)

def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add a student")
        print("2. View all students")
        print("3. Edit a student's information")
        print("4. Filter students by address")
        print("5. Delete a student")
        print("6. Exit the program")
        choice = input("Choose an option: ")

        if choice == '1':
            print("\nEnter student information:")
            student = input_student()
            add_student(student)
            print("Student information has been added!")
        elif choice == '2':
            print("\n--- Student List ---")
            view_students()
        elif choice == '3':
            student_id = input("Enter the index of the student to edit: ")
            first_name = input("Enter the new first name (leave blank to skip): ")
            last_name = input("Enter the new last name (leave blank to skip): ")
            home_address = input("Enter the new home address (leave blank to skip): ")
            school_address = input("Enter the new school address (leave blank to skip): ")

            edit_student(int(student_id), first_name or None, last_name or None, home_address or None, school_address or None)
        elif choice == '4':
            address_type = input("Enter the address type to filter (home or school): ").strip().lower()
            address_value = input("Enter the city to filter by: ").strip()
            filter_students_by_address(address_type, address_value)
        elif choice == '5':
            student_id = input("Enter the index of the student to delete: ")
            delete_student(int(student_id))
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again!")

main_menu()