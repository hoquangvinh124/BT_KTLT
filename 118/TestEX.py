import numpy as np
import pyqtgraph as pg
from Test import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.plot_data)
        self.plotWidget = pg.PlotWidget()
        self.verticalLayout.addWidget(self.plotWidget)

    def plot_data(self):
        text_data = self.lineEdit.text()
        y_values = list(map(float, text_data.split(',')))
        x_values = np.arange(len(y_values))
        self.plotWidget.clear()
        self.plotWidget.setBackground('black')
        pen = pg.mkPen(color='blue', width=2)
        self.plotWidget.plot(x_values, y_values, pen=pen, symbol='o', symbolBrush='blue')

    def show(self):
        self.MainWindow.show()



