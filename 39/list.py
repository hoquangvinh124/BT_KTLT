# Form implementation generated from reading ui file 'D:\ToiDiDaoCode\39\list.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 473)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 151, 31))
        self.label_2.setObjectName("label_2")
        self.nInput = QtWidgets.QLineEdit(parent=Form)
        self.nInput.setGeometry(QtCore.QRect(32, 60, 137, 22))
        self.nInput.setObjectName("nInput")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(12, 60, 16, 16))
        self.label.setObjectName("label")
        self.createRandomBtn = QtWidgets.QPushButton(parent=Form)
        self.createRandomBtn.setGeometry(QtCore.QRect(190, 60, 95, 28))
        self.createRandomBtn.setObjectName("createRandomBtn")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(12, 89, 281, 341))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 339))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.deleteBtn = QtWidgets.QPushButton(parent=Form)
        self.deleteBtn.setGeometry(QtCore.QRect(310, 200, 93, 28))
        self.deleteBtn.setObjectName("deleteBtn")
        self.ascSortBtn = QtWidgets.QPushButton(parent=Form)
        self.ascSortBtn.setGeometry(QtCore.QRect(310, 250, 93, 28))
        self.ascSortBtn.setObjectName("ascSortBtn")
        self.descSortBtn = QtWidgets.QPushButton(parent=Form)
        self.descSortBtn.setGeometry(QtCore.QRect(310, 300, 93, 28))
        self.descSortBtn.setObjectName("descSortBtn")
        self.removeAllBtn = QtWidgets.QPushButton(parent=Form)
        self.removeAllBtn.setGeometry(QtCore.QRect(310, 350, 93, 28))
        self.removeAllBtn.setObjectName("removeAllBtn")
        self.addBtn = QtWidgets.QPushButton(parent=Form)
        self.addBtn.setGeometry(QtCore.QRect(310, 100, 93, 28))
        self.addBtn.setObjectName("addBtn")
        self.updateBtn = QtWidgets.QPushButton(parent=Form)
        self.updateBtn.setGeometry(QtCore.QRect(310, 150, 93, 28))
        self.updateBtn.setObjectName("updateBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "List Operations"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">List Operations</span></p></body></html>"))
        self.nInput.setText(_translate("Form", "50"))
        self.label.setText(_translate("Form", "N:"))
        self.createRandomBtn.setText(_translate("Form", "Create random"))
        self.deleteBtn.setText(_translate("Form", "Delete"))
        self.ascSortBtn.setText(_translate("Form", "Asc Sort"))
        self.descSortBtn.setText(_translate("Form", "Desc Sort"))
        self.removeAllBtn.setText(_translate("Form", "Remove All"))
        self.addBtn.setText(_translate("Form", "Add"))
        self.updateBtn.setText(_translate("Form", "Update"))
