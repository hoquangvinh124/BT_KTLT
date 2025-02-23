from School_Mangement_Class import SchoolManagement

def main():
    sm = SchoolManagement()

    while True:
        print("\n========= MENU =========")
        print("1. Thêm Student")
        print("2. Sửa Student")
        print("3. Xóa Student")
        print("4. Thêm Class")
        print("5. Sửa Class")
        print("6. Xóa Class")
        print("7. Thêm Subject")
        print("8. Sửa Subject")
        print("9. Xóa Subject")
        print("10. Đăng ký môn học (Student -> Subject)")
        print("11. Hủy đăng ký môn học (Student -> Subject)")
        print("12. Xem danh sách lớp")
        print("13. Xem danh sách lớp cho mỗi môn học")
        print("14. Xem danh sách môn học cho mỗi lớp")
        print("15. Lưu dữ liệu (pickle)")
        print("16. Đọc dữ liệu (pickle)")
        print("17. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            sm.add_student()
        elif choice == '2':
            sm.edit_student()
        elif choice == '3':
            sm.delete_student()
        elif choice == '4':
            sm.add_class()
        elif choice == '5':
            sm.edit_class()
        elif choice == '6':
            sm.delete_class()
        elif choice == '7':
            sm.add_subject()
        elif choice == '8':
            sm.edit_subject()
        elif choice == '9':
            sm.delete_subject()
        elif choice == '10':
            sm.register_student_to_subject()
        elif choice == '11':
            sm.unregister_student_from_subject()
        elif choice == '12':
            sm.view_class_list_with_teacher()
        elif choice == '13':
            sm.view_class_list_for_each_registered_course()
        elif choice == '14':
            sm.view_courses_for_each_registered_class()
        elif choice == '15':
            sm.save_data()
        elif choice == '16':
            sm.load_data()
        elif choice == '17':
            print("Kết thúc chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

main()