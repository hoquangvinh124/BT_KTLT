# Form implementation generated from reading ui file 'D:\TDT!!!\106\shop.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(210, 9, 202, 28))
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 70, 271, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.productList = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.productList.setGeometry(QtCore.QRect(10, 10, 250, 300))
        self.productList.setMinimumSize(QtCore.QSize(250, 300))
        self.productList.setObjectName("productList")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.productsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.productsLabel.setGeometry(QtCore.QRect(11, 45, 50, 16))
        self.productsLabel.setObjectName("productsLabel")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(300, 140, 291, 141))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(parent=self.widget)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.idLabel)
        self.idEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.idEdit)
        self.nameLabel = QtWidgets.QLabel(parent=self.widget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameEdit)
        self.priceLabel = QtWidgets.QLabel(parent=self.widget)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.priceLabel)
        self.priceEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.priceEdit.setObjectName("priceEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.priceEdit)
        self.statusLayout = QtWidgets.QHBoxLayout()
        self.statusLayout.setObjectName("statusLayout")
        self.priceLabel_2 = QtWidgets.QLabel(parent=self.widget)
        self.priceLabel_2.setObjectName("priceLabel_2")
        self.statusLayout.addWidget(self.priceLabel_2)
        self.priceEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.priceEdit_2.setObjectName("priceEdit_2")
        self.statusLayout.addWidget(self.priceEdit_2)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.statusLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.saveButton = QtWidgets.QPushButton(parent=self.widget)
        self.saveButton.setObjectName("saveButton")
        self.buttonLayout.addWidget(self.saveButton)
        self.removeButton = QtWidgets.QPushButton(parent=self.widget)
        self.removeButton.setObjectName("removeButton")
        self.buttonLayout.addWidget(self.removeButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.buttonLayout)
        self.productsLabel.raise_()
        self.scrollArea.raise_()
        self.titleLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Product Management"))
        self.titleLabel.setStyleSheet(_translate("MainWindow", "font-size: 16pt; color: blue;"))
        self.titleLabel.setText(_translate("MainWindow", "Product Management"))
        self.productsLabel.setText(_translate("MainWindow", "Products:"))
        self.idLabel.setText(_translate("MainWindow", "Id:"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.priceLabel.setText(_translate("MainWindow", "Price:"))
        self.priceLabel_2.setText(_translate("MainWindow", "Manufacturer:"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
