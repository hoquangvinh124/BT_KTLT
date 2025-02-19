from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from E68.ui.order_detail import Ui_OrderDetailDialog
from E68.class_information.OrderDetail import OrderDetail

class OrderDetailDialog(QDialog, Ui_OrderDetailDialog):
    def __init__(self, parent=None, main_window=None):
        super().__init__(parent)
        self.setupUi(self)

        self.main_window = main_window
        self.result_data = []

        if self.main_window:
            self.populate_categories()

        self.comboBoxCategories.currentIndexChanged.connect(self.update_products)
        self.btnAdd.clicked.connect(self.add_order_detail)
        self.btnSave.clicked.connect(self.save_order)

        self.tableOrderDetails.setColumnCount(2)
        self.tableOrderDetails.setHorizontalHeaderLabels(["Product", "Quantity"])

    def populate_categories(self):
        self.comboBoxCategories.clear()
        for category in self.main_window.categories:
            self.comboBoxCategories.addItem(category.name, category)

    def update_products(self):
        self.comboBoxProducts.clear()
        selected_category = self.comboBoxCategories.currentData()
        if selected_category:
            for product in selected_category.products:
                self.comboBoxProducts.addItem(product.product_name, product)

    def add_order_detail(self):
        selected_product = self.comboBoxProducts.currentData()
        quantity = self.spinBoxQuantity.value()

        if not selected_product:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn sản phẩm!")
            return

        row_count = self.tableOrderDetails.rowCount()
        self.tableOrderDetails.insertRow(row_count)
        self.tableOrderDetails.setItem(row_count, 0, QTableWidgetItem(selected_product.product_name))
        self.tableOrderDetails.setItem(row_count, 1, QTableWidgetItem(str(quantity)))

    def save_order(self):
        row_count = self.tableOrderDetails.rowCount()
        if row_count == 0:
            QMessageBox.warning(self, "Lỗi", "Không có sản phẩm nào trong Order!")
            return

        self.result_data = []
        for row in range(row_count):
            product_name = self.tableOrderDetails.item(row, 0).text()
            quantity = int(self.tableOrderDetails.item(row, 1).text())

            selected_product = None
            for category in self.main_window.categories:
                for product in category.products:
                    if product.product_name == product_name:
                        selected_product = product
                        break

            if selected_product:
                order_detail = OrderDetail(
                    orderID=self.main_window.lineEdit.text(),
                    productID=selected_product.product_id,
                    unitPrice=selected_product.unit_price,
                    quantity=quantity,
                    discount=0.0
                )
                self.result_data.append(order_detail)

        self.accept()

    def get_result(self):
        return self.result_data
