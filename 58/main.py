from employee_class import Employee

def input_employee():
    last_name = input("Nhập họ: ")
    first_name = input("Nhập tên: ")
    num_products = int(input("Nhập số sản phẩm: "))
    return Employee(last_name, first_name, num_products)

def compare_employees(emp1, emp2):
    if emp1.is_higher(emp1):
        print("Nhân viên 1 có số sản phẩm nhiều hơn.")
    elif emp2.is_higher(emp1):
        print("Nhân viên 2 có số sản phẩm nhiều hơn.")
    else:
        print("Cả hai nhân viên có số sản phẩm bằng nhau.")

def main_menu():
    while True:
        print("\n--- MENU ---")
        print("1. Nhập thông tin 2 nhân viên")
        print("2. So sánh số sản phẩm và lương")
        print("3. Thoát chương trình")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            global emp1, emp2
            print("\nNhập thông tin nhân viên 1:")
            emp1 = input_employee()
            print("\nNhập thông tin nhân viên 2:")
            emp2 = input_employee()
            print("Thông tin nhân viên đã được nhập!")
        elif choice == '2':
            try:
                compare_employees(emp1, emp2)
            except NameError:
                print("Bạn cần nhập thông tin nhân viên trước!")
        elif choice == '3':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

main_menu()