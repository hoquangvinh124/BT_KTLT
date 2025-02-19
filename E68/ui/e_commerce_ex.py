from E68.class_information.Order import Order
from E68.class_information.Test import create_sample_data
from E68.ui.e_commerce import Ui_MainWindow
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow, QDialog, QWidget
from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QTabWidget

class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        (self.categories, self.products, self.employees, self.customers,
         self.orders) = create_sample_data()
        self.list_of_orders = [o for o in self.orders]

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.set_combobox_info()
        self.create_button(self.list_of_orders)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.add_order)
        self.pushButton_3.clicked.connect(self.show_data_overview)
        self.pushButton_2.clicked.connect(self.remove_by_id)

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
        for order in list:
            btn = QPushButton(order.print_information())
            btn.clicked.connect(lambda _, o=order: self.show_orders_details(o))
            self.verticalLayoutButton.addWidget(btn)

    def show_orders_details(self, o):
        self.lineEdit.setText(f"{o.orderID}")

    def add_order(self):
        customer = self.comboBox.currentData()
        employee = self.comboBox_2.currentData()
        order_id = self.lineEdit.text()
        exist = False
        for order in self.list_of_orders:
            if order_id == str(order.orderID):
                exist = True
                print("Ban phai xoa order cu truoc khi them (trung id)")
        if not exist:
            order_completed = None
            from E68.ui.order_detail_ex import OrderDetailDialog
            dialog = OrderDetailDialog(parent=self, main_window=self)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                order_details = dialog.get_result()
                order_completed = Order(order_id, customer.customerID, employee.employeeID)
                for od in order_details:
                    order_completed.add_order_detail(od)
            if order_completed:
                self.list_of_orders.append(order_completed)
        self.create_button(self.list_of_orders)

    def set_combobox_info(self):
        for c in self.customers:
            self.comboBox.addItem(c.get_info(), c)
        for e in self.employees:
            self.comboBox_2.addItem(e.get_info(), e)

    def remove_by_id(self):
        orderID = str(self.lineEdit.text())
        success = False
        for i, o in enumerate(self.list_of_orders):
            if str(o.orderID) == orderID:
                self.list_of_orders.pop(i)
                success = True
        if not success:
            print("ID not found to delete")
        self.create_button(self.list_of_orders)

    def show_data_overview(self):
        dialog = DataOverviewDialog(
            self.categories, self.employees, self.customers, self.list_of_orders,
            parent=self
        )
        dialog.exec()

    def show(self):
        self.MainWindow.show()

class DataOverviewDialog(QDialog):
    def __init__(self, categories, employees, customers, orders, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Thông tin")
        self.resize(600, 400)
        layout = QVBoxLayout(self)

        self.tab_widget = QTabWidget(self)
        layout.addWidget(self.tab_widget)

        self.create_categories_tab(categories)
        self.create_employees_tab(employees)
        self.create_customers_tab(customers)
        self.create_orders_tab(orders)

    def create_categories_tab(self, categories):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        list_widget = QListWidget()
        tab_layout.addWidget(list_widget)

        for cat in categories:
            list_widget.addItem(QListWidgetItem(str(cat)))
            for prod in cat.products:
                list_widget.addItem(QListWidgetItem("   " + str(prod)))

        self.tab_widget.addTab(tab, "Categories")

    def create_employees_tab(self, employees):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        list_widget = QListWidget()
        tab_layout.addWidget(list_widget)

        for emp in employees:
            list_widget.addItem(QListWidgetItem(str(emp)))

        self.tab_widget.addTab(tab, "Employees")

    def create_customers_tab(self, customers):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        list_widget = QListWidget()
        tab_layout.addWidget(list_widget)

        for cus in customers:
            list_widget.addItem(QListWidgetItem(str(cus)))

        self.tab_widget.addTab(tab, "Customers")

    def create_orders_tab(self, orders):
        tab = QWidget()
        tab_layout = QVBoxLayout(tab)
        list_widget = QListWidget()
        tab_layout.addWidget(list_widget)

        for odr in orders:
            list_widget.addItem(QListWidgetItem(str(odr)))
            for detail in odr.orderDetails:
                list_widget.addItem(QListWidgetItem("   " + str(detail)))

        self.tab_widget.addTab(tab, "Orders")

def show_data_overview(self):
    dialog = DataOverviewDialog(
        self.categories, self.employees, self.customers, self.orders,
        parent=self
    )
    dialog.exec()

