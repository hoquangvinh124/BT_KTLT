from E80.FileFactory import *
from E80.Product import *
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QMessageBox, QDialog, QLabel, QInputDialog
from E80.ui.shop import Ui_MainWindow
from E80.TestReadData import sort_products, sort_products_desc


class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(FileFactory.read_data("../database.txt"))
        self.saveButton.clicked.connect(self.change_information)
        self.removeButton.clicked.connect(self.remove_by_id)
        self.filterButton.clicked.connect(self.desc_sort)
        self.searchButton.clicked.connect(self.asc_sort)

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
        for product in list:
            btn = QPushButton(product.get_info())
            btn.clicked.connect(lambda _, p=product: self.show_product_details(p))
            self.verticalLayoutButton.addWidget(btn)

    def show_product_details(self, product):
        self.idEdit.setText(f"{product.product_id}")
        self.nameEdit.setText(f"{product.product_name}")
        self.priceEdit.setText(f"{product.unit_price}")

    def change_information(self):
        id = str(self.idEdit.text())
        name = str(self.nameEdit.text())
        price = str(self.priceEdit.text())
        product = Product(id, name, float(price))
        if FileFactory.check_product_exists("../database.txt", id):
            FileFactory.edit_data("../database.txt", id, product)
        else:
            FileFactory.write_data("../database.txt", product)
        self.create_button(FileFactory.read_data("../database.txt"))

    def remove_by_id(self):
        id = str(self.idEdit.text())
        if FileFactory.check_product_exists("../database.txt", id):
            FileFactory.delete_product("../database.txt", id)
        self.create_button(FileFactory.read_data("../database.txt"))

    def asc_sort(self):
        curr = FileFactory.read_data("../database.txt")
        new_arr = sort_products(curr)
        self.create_button(new_arr)

    def desc_sort(self):
        curr = FileFactory.read_data("../database.txt")
        new_arr = sort_products_desc(curr)
        self.create_button(new_arr)

    def show(self):
        self.MainWindow.show()