from Array import Ui_MainWindow
import random

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.array = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_ra.clicked.connect(self.generate_random_array)
        self.pushButton_se.clicked.connect(self.find_smallest)
        self.pushButton_idv.clicked.connect(self.increment_double)
        self.pushButton_coe.clicked.connect(self.count_odd)
        self.pushButton_sascending.clicked.connect(self.sort_ascending)
        self.pushButton_sdescending.clicked.connect(self.sort_descending)
        self.pushButton_sooe.clicked.connect(self.sum_odd)
        self.pushButton_soa.clicked.connect(self.sum_array)

    def generate_random_array(self):
        self.array = [random.randint(1, 100) for _ in range(10)]
        self.label_o.setText(' '.join(map(str, self.array)))
        self.label_r.clear()

    def find_smallest(self):
        if self.array:
            smallest = min(self.array)
            self.label_r.setText(f"Smallest element: {smallest}")

    def sum_array(self):
        if self.array:
            total = sum(self.array)
            self.label_r.setText(f"Sum of Array = {total}")

    def increment_double(self):
        if self.array:
            self.array = [x * 2 for x in self.array]
            self.label_o.setText(' '.join(map(str, self.array)))
            self.label_r.setText("Doubled")

    def count_odd(self):
        if self.array:
            odd_count = sum(1 for x in self.array if x % 2 != 0)
            self.label_r.setText(f"Number of odd elements: {odd_count}")

    def sort_ascending(self):
        if self.array:
            self.array.sort()
            self.label_r.setText(' '.join(map(str, self.array)))

    def sort_descending(self):
        if self.array:
            self.array.sort(reverse=True)
            self.label_r.setText(' '.join(map(str, self.array)))

    def sum_odd(self):
        if self.array:
            odd_sum = sum(x for x in self.array if x % 2 != 0)
            self.label_r.setText(f"Sum of odd elements: {odd_sum}")

    def show(self):
        self.MainWindow.show()
