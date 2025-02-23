class EmployeeAsset:
    def __init__(self, employee_id, asset_id, role):
        self.employee_id = employee_id
        self.asset_id = asset_id
        self.role = role

    def __str__(self):
        return f"{self.employee_id}\t{self.asset_id}\t{self.role}"