from PyQt6.QtWidgets import QPushButton, QMessageBox, QMainWindow
from E85.Lib.DataConnector import DataProcessing
from E85.Lib.JsonFileFactory import JsonFileFactory
from E85.ClassInfo.Asset import Asset
from E85.ui.MainPage import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.current_user = None
        self.selected_asset = None
        self.assets = []

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonRemove.clicked.connect(self.delete_button)
        self.pushButtonSave.clicked.connect(self.save_button)

    def handle_login(self, emp):
        self.current_user = emp
        self.create_button()

    def showWindow(self):
        self.MainWindow.show()

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def create_button(self):
        self.clearLayout(self.verticalLayoutButton)
        asset_list = DataProcessing.retrieve_asset_for_each_employee(self.current_user)
        for asset in asset_list:
            btn = QPushButton(str(asset))
            btn.clicked.connect(lambda _, a=asset: self.show_asset_details(a))
            self.verticalLayoutButton.addWidget(btn)

    def show_asset_details(self, a):
        self.lineEditId.setText(a.asset_id)
        self.lineEditName.setText(a.asset_name)
        self.lineEditYear.setText(str(a.import_year))
        self.lineEditValue.setText(str(a.value))
        self.selected_asset = a

    def delete_button(self):
        msp = self.lineEditId.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Bạn muốn xóa tài sản {msp} ?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.No:
            return
        if self.selected_asset is not None:
            jff = JsonFileFactory()
            filename = "../DataSet/assets.json"
            all_assets = jff.read_data(filename, Asset)
            for a in all_assets:
                if a.asset_id == self.selected_asset.asset_id:
                    all_assets.remove(a)
                    break
            jff.write_data(all_assets, filename)
            self.create_button()

    def save_button(self):
        id = self.lineEditId.text()
        name = self.lineEditName.text()
        year = int(self.lineEditYear.text())
        value = int(self.lineEditValue.text())
        a = Asset(id, name, year, value)
        jff = JsonFileFactory()
        filename = "../DataSet/assets.json"
        all_assets = jff.read_data(filename, Asset)
        all_assets.append(a)
        jff.write_data(all_assets, filename)
        self.create_button()

