import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem
from Dataset import Dataset
from FileFactory import FileFactory
from ProductM import Ui_MainWindow
from Product import Product


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_factory = FileFactory()
        self.dataset = None
        self.selected_catalog = None
        self.selected_product = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.dataset = self.file_factory.readData("database.json", Dataset)
        self.dataset.re_model()
        self.load_catalog_for_combo_box()
        self.cboCatalog.activated.connect(self.process_selected_catalog)
        self.listWidgetProduct.itemSelectionChanged.connect(self.process_selected_product)
        self.pushButtonNew.clicked.connect(self.process_new)
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonDelete.clicked.connect(self.process_delete)

    def load_catalog_for_combo_box(self):
        for i in range(self.dataset.size()):
            catalog = self.dataset.item(i)
            self.cboCatalog.addItem(str(catalog), catalog)

    def process_selected_catalog(self):
        self.selected_catalog = self.cboCatalog.currentData(Qt.ItemDataRole.UserRole)
        self.listWidgetProduct.clear()
        for i in range(self.selected_catalog.size()):
            product = self.selected_catalog.item(i)
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, product)
            item.setText(str(product))
            self.listWidgetProduct.addItem(item)

    def process_selected_product(self):
        current_row = self.listWidgetProduct.currentRow()
        if current_row < 0:
            return
        item = self.listWidgetProduct.item(current_row)
        self.selected_product = item.data(Qt.ItemDataRole.UserRole)
        self.lineEditProductId.setText(str(self.selected_product.id))
        self.lineEditProductName.setText(self.selected_product.name)
        self.lineEditUnitPrice.setText(str(self.selected_product.price))
        date_format = '%Y-%m-%d %H:%M:%S'
        timetracking = datetime.datetime.strptime(self.selected_product.timetracking, date_format)
        self.dateTimeEditTracking.setDateTime(timetracking)

    def process_new(self):
        self.lineEditProductId.setText("")
        self.lineEditProductName.setText("")
        self.lineEditUnitPrice.setText("")
        self.selected_product = None
        self.lineEditProductId.setFocus()

    def process_save(self):
        if self.selected_catalog is None:
            return
        product_id = int(self.lineEditProductId.text())
        name = self.lineEditProductName.text()
        price = float(self.lineEditUnitPrice.text())
        tracking = self.dateTimeEditTracking.dateTime()
        date_format = '%Y-%m-%d %H:%M:%S'
        tracking_format = tracking.toPyDateTime().strftime(date_format)

        product = Product(product_id, name, price, tracking_format)
        item = QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole, product)
        item.setText(str(product))
        if self.selected_product is None:
            self.selected_product = product
            self.selected_catalog.add(product)
            self.listWidgetProduct.addItem(item)
        else:
            index = self.selected_catalog.index(self.selected_product)
            self.selected_product = product
            self.selected_catalog.update(index, self.selected_product)
            item = self.listWidgetProduct.item(index)
            item.setData(Qt.ItemDataRole.UserRole, self.selected_product)
            item.setText(str(self.selected_product))
        self.file_factory.writeData("database.json", self.dataset)

    def process_delete(self):
        if self.selected_product is not None:
            self.selected_catalog.removeByItem(self.selected_product)
            self.file_factory.writeData("database.json", self.dataset)
            self.process_selected_catalog()
            self.process_new()

    def show(self):
        self.MainWindow.show()
