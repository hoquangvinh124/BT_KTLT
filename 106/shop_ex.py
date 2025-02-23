from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from shop import Ui_MainWindow
from ClassInfo import *
from FileUtil import *

class MainWindowEx(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ListOfProduct = ListOfProduct()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.data_load()
        self.create_button(self.ListOfProduct.arr)
        self.saveButton.clicked.connect(self.change_information)
        self.removeButton.clicked.connect(self.remove_by_id)

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
            btn = QPushButton(product.__str__())
            btn.clicked.connect(lambda _, p=product: self.show_product_details(p))
            self.verticalLayoutButton.addWidget(btn)

    def show_product_details(self, product):
        self.idEdit.setText(f"{product.id}")
        self.nameEdit.setText(f"{product.name}")
        self.priceEdit_2.setText(f"{product.manufacturer}")
        self.priceEdit.setText(f"{product.price}")

    def change_information(self):
        id = str(self.idEdit.text())
        name = str(self.nameEdit.text())
        price = str(self.priceEdit.text())
        manufacturer = str(self.priceEdit_2.text())
        found = False
        for e in self.ListOfProduct.arr:
            if e.id == id:
                e.id = id
                e.name = name
                e.manufacturer = manufacturer
                e.price = price
                found = True
        if not found:
            self.ListOfProduct.add_product(Product(id, name, manufacturer, price))
        FileUtil.saveModel(self.ListOfProduct.arr, "product.pkl")
        self.create_button(self.ListOfProduct.arr)

    def remove_by_id(self):
        id = str(self.idEdit.text())
        self.create_button(self.ListOfProduct.remove_product(id))
        FileUtil.saveModel(self.ListOfProduct.arr, "product.pkl")

    def data_load(self):
        data = FileUtil.loadModel("product.pkl")
        for i in data:
            self.ListOfProduct.add_product(i)


    def show(self):
        self.MainWindow.show()