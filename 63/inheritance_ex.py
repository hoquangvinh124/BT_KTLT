from inheritance import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QInputDialog, QWidget
from class_info import *

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.list_product = ListOfProduct()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.create_button(self.list_product.arr)
        self.saveButton.clicked.connect(self.change_information)
        self.removeButton.clicked.connect(self.remove_product)
        self.filterButton.clicked.connect(self.filter_price)
        self.searchButton.clicked.connect(self.search_name)

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
            btn = QPushButton(product.display_info())
            btn.clicked.connect(lambda _, p=product: self.show_product_details(p))
            self.verticalLayoutButton.addWidget(btn)

    def show_product_details(self, product):
        self.idEdit.setText(f"{product.code}")
        self.nameEdit.setText(f"{product.name}")
        self.priceEdit.setText(f"{product.price}")
        self.discountEdit.setText(f"{product.discount}")

    def change_information(self):
        id = str(self.idEdit.text())
        name = str(self.nameEdit.text())
        price = str(self.priceEdit.text())
        try:
            price = float(price) if "." in price else int(price)
        except ValueError:
            price = 0
        found = False
        for product in self.list_product.arr:
            if product.code == id:
                product.code = id
                product.name = name
                product.price = price
                found = True
        if not found:
            if self.officialRadio.isChecked():
                obj = OfficialProduct(id, name, price)
                self.list_product.add_product(obj)
            if self.notOfficialRadio.isChecked():
                obj = NonOfficialProduct(id, name, price)
                self.list_product.add_product(obj)
        self.create_button(self.list_product.arr)

    def search_name(self):
        name, confirm = QInputDialog.getText(self.MainWindow, "Enter name", "Enter Name:")
        if confirm:
            self.create_button(self.list_product.search_name(name))

    def filter_price(self):
        price, confirm = QInputDialog.getText(self.MainWindow, "Enter price", "Enter Price :")
        if confirm:
            self.create_button(self.list_product.filter_price(float(price)))

    def remove_product(self):
        id = self.idEdit.text()
        self.create_button(self.list_product.remove_product(id))

    def show(self):
        self.MainWindow.show()