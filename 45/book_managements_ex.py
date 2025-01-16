

from book_managements import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLineEdit, QDialog, QLabel, QDialogButtonBox, QWidget


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.books = [
    ('112', 'Basic Python', 'Hồ Quang Vinh', '2020', 'VNU'),
    ('113', 'Advance Python', 'Quang Vinh Hồ', '2020', 'ABC'),
    ('114', 'Machine learing', 'Vinh Hồ Quang', '2024', 'VNU'),
    ('115', 'DJango', 'Hồ Vinh Quang', '2023', 'VNU'),
    ('111', 'Mobile', 'Vinh Quang Hồ', '2022', 'Lucy')
]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(self.books)
        self.pushButton.clicked.connect(self.change_information)
        self.pushButton_3.clicked.connect(self.search_title)
        self.pushButton_5.clicked.connect(self.filter_years)
        self.pushButton_4.clicked.connect(self.search_isbn)
        self.pushButton_6.clicked.connect(self.filter_publisher)
        self.pushButton_2.clicked.connect(self.remove_book)

    def search_isbn(self):
        search_isbn = self.open_input_dialog()
        filtered_books = [book for book in self.books if search_isbn in book[0]]
        self.clear_layout(self.verticalLayoutButton)
        self.create_button(filtered_books)

    def filter_years(self):
        search_publisher = self.open_input_dialog()
        filtered_books = [book for book in self.books if search_publisher in book[3]]
        self.clear_layout(self.verticalLayoutButton)
        self.create_button(filtered_books)

    def search_title(self):
        search_title = self.open_input_dialog()
        filtered_books = [book for book in self.books if search_title.lower() in book[1].lower()]
        self.clear_layout(self.verticalLayoutButton)
        self.create_button(filtered_books)

    def filter_publisher(self):
        search_publisher = self.open_input_dialog()
        filtered_books = [book for book in self.books if search_publisher.lower() in book[4].lower()]
        self.clear_layout(self.verticalLayoutButton)
        self.create_button(filtered_books)

    def remove_book(self):
        isbn = str(self.lineEdit.text())
        success = False
        for i, book in enumerate(self.books):
            if book[0] == isbn:
                self.books.pop(i)
                success = True
        if not success:
            print("ISBN not found to delete")
        self.create_button(self.books)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_layout(item.layout())

    def create_button(self, list):
        self.clear_layout(self.verticalLayoutButton)
        print()
        for book in list:
            print(book)
            content = f"ISBN:{book[0]}, {book[1]}, {book[3]}, {book[4]}"
            btn = QPushButton(content)
            btn.setObjectName(f"btn_{book[0]}")
            btn.clicked.connect(lambda _, b=book: self.show_book_details(b))
            self.verticalLayoutButton.addWidget(btn)

    def show_book_details(self, book):
        self.lineEdit.setText(f"{book[0]}")
        self.lineEdit_2.setText(f"{book[1]}")
        self.lineEdit_3.setText(f"{book[2]}")
        self.lineEdit_4.setText(f"{book[3]}")
        self.lineEdit_5.setText(f"{book[4]}")

    def change_information(self):
        isbn = str(self.lineEdit.text())
        title = str(self.lineEdit_2.text())
        author = str(self.lineEdit_3.text())
        year = str(self.lineEdit_4.text())
        publisher = str(self.lineEdit_5.text())
        found = False
        for i, book in enumerate(self.books):
            if book[0] == isbn:
                self.books[i] = (isbn, title, author, year, publisher)
                found = True
        if not found:
            self.books.append((isbn, title, author, year, publisher))
        self.create_button(self.books)

    def open_input_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Information")
        dialog.setModal(True)

        layout = QVBoxLayout()

        label = QLabel("Enter information: ")
        input_field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(input_field)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(buttons)
        dialog.setLayout(layout)
        user_input = ""

        def on_accept():
            nonlocal user_input
            user_input = input_field.text()
            dialog.accept()
        buttons.accepted.connect(on_accept)
        buttons.rejected.connect(dialog.reject)
        dialog.exec()
        return user_input


    def show(self):
        self.MainWindow.show()