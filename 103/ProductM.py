# Form implementation generated from reading ui file 'D:\TDT!!!\103\ProductM.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 408)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 30, 351, 271))
        self.groupBox.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 111, 20))
        self.label_3.setObjectName("label_3")
        self.lineEditProductId = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditProductId.setGeometry(QtCore.QRect(100, 50, 221, 22))
        self.lineEditProductId.setObjectName("lineEditProductId")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 151, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditProductName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditProductName.setGeometry(QtCore.QRect(100, 100, 221, 22))
        self.lineEditProductName.setObjectName("lineEditProductName")
        self.lineEditUnitPrice = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditUnitPrice.setGeometry(QtCore.QRect(100, 150, 221, 22))
        self.lineEditUnitPrice.setObjectName("lineEditUnitPrice")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.label_6.setObjectName("label_6")
        self.dateTimeEditTracking = QtWidgets.QDateTimeEdit(parent=self.groupBox)
        self.dateTimeEditTracking.setGeometry(QtCore.QRect(100, 200, 221, 31))
        self.dateTimeEditTracking.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 29), QtCore.QTime(0, 0, 0)))
        self.dateTimeEditTracking.setCalendarPopup(True)
        self.dateTimeEditTracking.setObjectName("dateTimeEditTracking")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 39, 251, 341))
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidgetProduct = QtWidgets.QListWidget(parent=self.groupBox_2)
        self.listWidgetProduct.setGeometry(QtCore.QRect(10, 100, 231, 221))
        self.listWidgetProduct.setStyleSheet("background-color: rgb(237, 255, 202);")
        self.listWidgetProduct.setObjectName("listWidgetProduct")
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.label.setObjectName("label")
        self.cboCatalog = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cboCatalog.setGeometry(QtCore.QRect(10, 40, 221, 22))
        self.cboCatalog.setStyleSheet("background-color: rgb(237, 255, 202);")
        self.cboCatalog.setObjectName("cboCatalog")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 300, 351, 81))
        self.groupBox_3.setStyleSheet("background-color: rgb(249, 255, 210);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonNew = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonNew.setGeometry(QtCore.QRect(10, 30, 93, 41))
        self.pushButtonNew.setStyleSheet("background-color: rgb(170, 255, 127);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\TDT!!!\\103\\images/ic_new.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonNew.setIcon(icon)
        self.pushButtonNew.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonNew.setObjectName("pushButtonNew")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSave.setGeometry(QtCore.QRect(120, 30, 93, 41))
        self.pushButtonSave.setStyleSheet("background-color: rgb(170, 255, 127);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\TDT!!!\\103\\images/ic_save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonSave.setIcon(icon1)
        self.pushButtonSave.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonDelete = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonDelete.setGeometry(QtCore.QRect(232, 30, 111, 41))
        self.pushButtonDelete.setStyleSheet("background-color: rgb(170, 255, 127);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\TDT!!!\\103\\images/ic_delete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonDelete.setIcon(icon2)
        self.pushButtonDelete.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 0, 301, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product"))
        self.groupBox.setTitle(_translate("MainWindow", "Product Details:"))
        self.label_3.setText(_translate("MainWindow", "Product ID:"))
        self.label_4.setText(_translate("MainWindow", "Product Name:"))
        self.label_5.setText(_translate("MainWindow", "Unit Price:"))
        self.label_6.setText(_translate("MainWindow", "Time Tracking:"))
        self.dateTimeEditTracking.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm:ss"))
        self.label.setText(_translate("MainWindow", "Select a Catalog:"))
        self.label_2.setText(_translate("MainWindow", "List of Products:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Action:"))
        self.pushButtonNew.setText(_translate("MainWindow", "New"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.label_7.setText(_translate("MainWindow", "Product Management"))
