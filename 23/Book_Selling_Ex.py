from Book_Selling import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.revenue = 0
        self.total_students = 0
        self.total_customer = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_Calculate.clicked.connect(self.calculate_payment)
        self.pushButton_NSelling.clicked.connect(self.new_selling)
        self.pushButton_Statistics.clicked.connect(self.statistic)


    def check(self):
        customer_name = self.customer_name.text()
        if not customer_name.strip():
            self.customer_name.setText("Customer name cannot be empty!")
            return False
        quantity = self.quantity.text()
        if not quantity.strip():
            self.quantity.setText("0")
            return False
        quantity = int(self.quantity.text())
        if quantity <= 0:
            self.quantity.setText("0")
            return False
        return True

    def calculate_payment(self):
        if self.check():
            quantity = int(self.quantity.text())
            unit_price = 20000
            total_payment = quantity * unit_price

            if self.checkBox.isChecked():
                self.total_students += 1
                total_payment *= 0.95

            self.total_customer += 1
            self.revenue += total_payment
            self.payment.setText(f"{total_payment:.0f}")

    def new_selling(self):
        self.customer_name.clear()
        self.quantity.setText("0")
        self.checkBox.setChecked(False)

    def statistic(self):
        self.total_customers.setText(f"{self.total_customer}")
        self.Total_revenue.setText(f"{self.revenue:.0f}")
        self.number_of_students.setText(f"{self.total_students}")

    def show(self):
        self.MainWindow.show()
