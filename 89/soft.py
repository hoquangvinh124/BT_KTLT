# Form implementation generated from reading ui file 'D:\TDT!!!\89\soft.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 335)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 400, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBoxDetails = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBoxDetails.setGeometry(QtCore.QRect(420, 40, 350, 261))
        self.groupBoxDetails.setObjectName("groupBoxDetails")
        self.label_ID = QtWidgets.QLabel(parent=self.groupBoxDetails)
        self.label_ID.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_ID.setObjectName("label_ID")
        self.lineEdit_ID = QtWidgets.QLineEdit(parent=self.groupBoxDetails)
        self.lineEdit_ID.setGeometry(QtCore.QRect(100, 30, 200, 21))
        self.lineEdit_ID.setReadOnly(False)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.label_FullName = QtWidgets.QLabel(parent=self.groupBoxDetails)
        self.label_FullName.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_FullName.setObjectName("label_FullName")
        self.lineEdit_FullName = QtWidgets.QLineEdit(parent=self.groupBoxDetails)
        self.lineEdit_FullName.setGeometry(QtCore.QRect(100, 80, 200, 21))
        self.lineEdit_FullName.setReadOnly(False)
        self.lineEdit_FullName.setObjectName("lineEdit_FullName")
        self.label_Address = QtWidgets.QLabel(parent=self.groupBoxDetails)
        self.label_Address.setGeometry(QtCore.QRect(10, 130, 81, 21))
        self.label_Address.setObjectName("label_Address")
        self.lineEdit_Address = QtWidgets.QLineEdit(parent=self.groupBoxDetails)
        self.lineEdit_Address.setGeometry(QtCore.QRect(100, 130, 200, 21))
        self.lineEdit_Address.setReadOnly(False)
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.label_Birth = QtWidgets.QLabel(parent=self.groupBoxDetails)
        self.label_Birth.setGeometry(QtCore.QRect(10, 180, 81, 21))
        self.label_Birth.setObjectName("label_Birth")
        self.lineEdit_Birth = QtWidgets.QLineEdit(parent=self.groupBoxDetails)
        self.lineEdit_Birth.setGeometry(QtCore.QRect(100, 180, 200, 21))
        self.lineEdit_Birth.setReadOnly(False)
        self.lineEdit_Birth.setObjectName("lineEdit_Birth")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBoxDetails)
        self.pushButton.setGeometry(QtCore.QRect(100, 223, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBoxDetails)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 223, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Management"))
        self.groupBoxDetails.setTitle(_translate("MainWindow", "Thông tin chi tiết"))
        self.label_ID.setText(_translate("MainWindow", "STT:"))
        self.label_FullName.setText(_translate("MainWindow", "Mã:"))
        self.label_Address.setText(_translate("MainWindow", "Tên:"))
        self.label_Birth.setText(_translate("MainWindow", "Tuổi:"))
        self.pushButton.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_2.setText(_translate("MainWindow", "Sắp xếp"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Danh sách nhân viên</span></p></body></html>"))
