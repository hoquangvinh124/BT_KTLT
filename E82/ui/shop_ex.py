from E82.TestXML.XMLTest import *
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget
from E82.ui.shop import Ui_MainWindow

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
        self.create_button(XMLFunction.read_xml("../products.xml"))
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
            btn = QPushButton(product.__str__())
            btn.clicked.connect(lambda _, p=product: self.show_product_details(p))
            self.verticalLayoutButton.addWidget(btn)

    def show_product_details(self, product):
        self.idEdit.setText(f"{product.id}")
        self.nameEdit.setText(f"{product.name}")
        self.priceEdit.setText(f"{product.price}")

    def change_information(self):
        id = str(self.idEdit.text())
        name = str(self.nameEdit.text())
        price = str(self.priceEdit.text())
        XMLFunction.find_to_edit_or_insert("../products.xml", id, name, price)
        self.create_button(XMLFunction.read_xml("../products.xml"))

    def remove_by_id(self):
        id = str(self.idEdit.text())
        try:
            XMLFunction.remove_xml("../products.xml", id)
        except ValueError:
            print("Not found ID to delete")
        self.create_button(XMLFunction.read_xml("../products.xml"))

    def asc_sort(self):
        curr = XMLFunction.read_xml("../products.xml")
        new_arr = XMLFunction.sort_products(curr)
        self.create_button(new_arr)

    def desc_sort(self):
        curr = XMLFunction.read_xml("../products.xml")
        new_arr = XMLFunction.sort_products_desc(curr)
        self.create_button(new_arr)

    def show(self):
        self.MainWindow.show()