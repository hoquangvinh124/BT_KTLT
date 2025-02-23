import numpy as np
from Test import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.calculate_statistics)

    def show(self):
        self.MainWindow.show()

    def calculate_statistics(self):
        text_data = self.lineEdit.text()
        numbers = list(map(float, text_data.replace(';', ',').split(',')))
        arr = np.array(numbers)
        min_val = np.min(arr)
        max_val = np.max(arr)
        mean_val = np.mean(arr)
        median_val = np.median(arr)
        std_dev = np.std(arr)
        result_text = (
            f"Min: {min_val:.2f}\n"
            f"Max: {max_val:.2f}\n"
            f"Mean: {mean_val:.2f}\n"
            f"Median: {median_val:.2f}\n"
            f"Std Dev: {std_dev:.2f}"
        )
        self.label_2.setText(result_text)


