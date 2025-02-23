from E85.Lib.JsonFileFactory import JsonFileFactory
from E85.ClassInfo.Employee import Employee
from E85.ClassInfo.Asset import Asset
from E85.ClassInfo.Employee_Asset import EmployeeAsset

class DataProcessing:
    @staticmethod
    def employees_retrieve():
        jff = JsonFileFactory()
        filename = "../DataSet/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    @staticmethod
    def assets_retrieve():
        jff = JsonFileFactory()
        filename = "../DataSet/assets.json"
        assets = jff.read_data(filename, Asset)
        return assets
    @staticmethod
    def employee_assets_retrieve():
        jff = JsonFileFactory()
        filename = "../DataSet/employee_assets.json"
        eas = jff.read_data(filename, EmployeeAsset)
        return eas
    @staticmethod
    def login_auth(username, password):
        employees = DataProcessing.employees_retrieve()
        for e in employees:
            if e.username == username and e.password == password:
                return e
        return None
    @staticmethod
    def retrieve_asset_for_each_employee(employee):
        eass = DataProcessing.employee_assets_retrieve()
        assets = DataProcessing.assets_retrieve()
        asset_dict = {asset.asset_id: asset for asset in assets}
        result = []
        for eas in eass:
            if eas.employee_id == employee.employee_id:
                asset = asset_dict.get(eas.asset_id)
                if asset:
                    result.append(asset)
        return result
