import random
from list import Ui_Form
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class MainWindowEx(Ui_Form):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.createRandomBtn.clicked.connect(self.createRandom)
        self.addBtn.clicked.connect(self.addButton)
        self.updateBtn.clicked.connect(self.updateButton)
        self.deleteBtn.clicked.connect(self.deleteNegative)
        self.ascSortBtn.clicked.connect(self.ascSort)
        self.descSortBtn.clicked.connect(self.descSort)
        self.removeAllBtn.clicked.connect(self.removeAll)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def createRandom(self):
        self.clearLayout(self.verticalLayoutButton)
        n = int(self.nInput.text())
        for i in range(n):
            x = random.randint(-100, 100)
            print(x)
            title = f"{x}"
            btn = QPushButton(text=title)
            self.verticalLayoutButton.addWidget(btn)

    def addButton(self):
        x = random.randint(0, 10)
        btn = QPushButton(text=str(x))
        self.verticalLayoutButton.addWidget(btn)

    def deleteNegative(self):
        for i in reversed(range(self.verticalLayoutButton.count())):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            if value < 0:
                self.verticalLayoutButton.removeWidget(button)
                button.deleteLater()

    def ascSort(self):
        buttons = []
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            buttons.append((value, button))
        buttons.sort(key=lambda x: x[0])
        for _, button in buttons:
            self.verticalLayoutButton.removeWidget(button)
        for _, button in buttons:
            self.verticalLayoutButton.addWidget(button)

    def descSort(self):
        buttons = []
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            buttons.append((value, button))
        buttons.sort(key=lambda x: x[0], reverse=True)
        for _, button in buttons:
            self.verticalLayoutButton.removeWidget(button)
        for _, button in buttons:
            self.verticalLayoutButton.addWidget(button)

    def removeAll(self):
        self.clearLayout(self.verticalLayoutButton)

    def updateButton(self):
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            current_value = int(button.text())
            new_value = current_value // 10
            button.setText(f"{new_value}")

    def show(self):
        self.MainWindow.show()