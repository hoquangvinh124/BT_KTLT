import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Test import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.set_up_plot()
        self.show_pie_chart()

    def set_up_plot(self):
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.verticalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canvas)

    def show_pie_chart(self):
        self.figure.clear()
        ax = self.figure.add_subplot()
        lbls = ['Chuyển nhượng BĐS', 'Cho thuê BĐS', 'DV khách sạn', 'Bệnh viện', 'Giáo dục', 'Sản xuất',
                'Hoạt động khác']
        income = [71.576, 6.788, 4.869, 2.675, 2.244, 18.007, 4.304]
        explode = [0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2]
        ax.pie(income, labels=lbls, explode=explode, autopct='%1.1f%%', pctdistance=1.1, labeldistance=1.2)
        ax.set_title('Cơ cấu doanh thu VinGroup - 2020', fontweight='bold')
        ax.legend(loc='upper right')
        self.canvas.draw()

    def show(self):
        self.MainWindow.show()
