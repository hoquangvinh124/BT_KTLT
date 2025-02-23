from PyQt6.QtWidgets import QTableWidgetItem
from shop import Ui_MainWindow
from DataProcessing import *
from PyQt6.QtCore import Qt

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.CategoryList = []
        self.ProductList = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.ProductList.extend(load_products())
        self.CategoryList.extend(load_categories())
        self.load_info_to_list_widget()
        self.listWidgetCategory.itemClicked.connect(self.load_data_table_widget)
        self.tableWidgetProducts.itemClicked.connect(self.display_products_details)

    def load_info_to_list_widget(self):
        for c in self.CategoryList:
            self.listWidgetCategory.addItem(c.name)

    def load_data_table_widget(self, item):
        category_info = item.text()
        matching_products = [p for p in self.ProductList if p.category == category_info]
        self.tableWidgetProducts.setRowCount(len(matching_products))
        self.tableWidgetProducts.setColumnCount(2)
        self.tableWidgetProducts.setHorizontalHeaderLabels(["Mã", "Tên"])
        for i, p in enumerate(matching_products):
            item_id = QTableWidgetItem(str(p.product_id))
            item_id.setData(Qt.ItemDataRole.UserRole, p)
            item_name = QTableWidgetItem(p.name)
            item_name.setData(Qt.ItemDataRole.UserRole, p)
            self.tableWidgetProducts.setItem(i, 0, item_id)
            self.tableWidgetProducts.setItem(i, 1, item_name)

    def display_products_details(self, item):
        obj = item.data(Qt.ItemDataRole.UserRole)
        self.lineEditMa.setText(str(obj.product_id))
        self.lineEditTenLinhKien.setText(obj.name)
        self.lineEditLoai.setText(obj.category)
        self.lineEditNhaSX.setText(obj.manufacturer)
        self.lineEditGia.setText(str(obj.unit_price))

    def show(self):
        self.MainWindow.show()