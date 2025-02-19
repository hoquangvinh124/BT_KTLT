import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox
from FileFactory import FileFactory
from FoodManagement import Ui_MainWindow
from Product import Product

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.arr_data = []
        self.file_factory = FileFactory()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.arr_data = self.file_factory.read_data("database.json", Product)
        self.show_product_into_q_list_widget()
        self.pushButtonNew.clicked.connect(self.process_new)
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonDelete.clicked.connect(self.process_delete)
        self.listWidgetProduct.itemSelectionChanged.connect(self.process_item_selection)

    def show_product_into_q_list_widget(self):
        self.listWidgetProduct.clear()
        for product in self.arr_data:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, product)
            item.setText(str(product))
            item.setCheckState(Qt.CheckState.Unchecked)
            if product.free_tax:
                item.setIcon(QIcon("images/ic_tax.png"))
            else:
                item.setIcon(QIcon("images/ic_tax_including.png"))
            if isinstance(product.expired_date, str):
                product.expired_date = datetime.date.fromisoformat(product.expired_date)
            days_left = (product.expired_date - datetime.date.today()).days
            if days_left <= 7:
                item.setForeground(Qt.GlobalColor.red)
            self.listWidgetProduct.addItem(item)

    def process_new(self):
        self.lineEditId.setText("")
        self.lineEditName.setText("")
        self.lineEditPrice.setText("")
        self.chkFreeTax.setCheckState(Qt.CheckState.Unchecked)
        self.lineEditId.setFocus()

    def check_duplicate(self, id_):
        items = [x for x in self.arr_data if x.product_id == id_]
        return items[0] if items else None

    def process_save(self):
        id_ = self.lineEditId.text()
        name = self.lineEditName.text()
        price = float(self.lineEditPrice.text())
        exp_date = self.dateEditExpiredDate.date().toPyDate()
        free_tax = self.chkFreeTax.isChecked()
        new_item = Product(id_, name, price, exp_date, free_tax)
        old_item = self.check_duplicate(id_)
        if old_item is not None:
            index = self.arr_data.index(old_item)
            self.arr_data[index] = new_item
        else:
            self.arr_data.append(new_item)
        self.show_product_into_q_list_widget()
        self.file_factory.write_data("database.json", self.arr_data)

    def process_delete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetProduct.count() - 1, -1, -1):
            item = self.listWidgetProduct.item(index)
            if item.checkState() == Qt.CheckState.Checked:
                product = item.data(Qt.ItemDataRole.UserRole)
                self.arr_data.remove(product)
        self.show_product_into_q_list_widget()
        self.file_factory.write_data("database.json", self.arr_data)

    def process_item_selection(self):
        row = self.listWidgetProduct.currentRow()
        item = self.listWidgetProduct.item(row)
        product = item.data(Qt.ItemDataRole.UserRole)
        self.lineEditId.setText(str(product.product_id))
        self.lineEditName.setText(product.product_name)
        self.lineEditPrice.setText(str(product.price))
        if isinstance(product.expired_date, str):
            product.expired_date = datetime.date.fromisoformat(product.expired_date)
        self.dateEditExpiredDate.setDate(product.expired_date)
        if product.free_tax:
            self.chkFreeTax.setCheckState(Qt.CheckState.Checked)
        else:
            self.chkFreeTax.setCheckState(Qt.CheckState.Unchecked)

    def show(self):
        self.MainWindow.show()
