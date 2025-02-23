class Asset:
    def __init__(self, asset_id, asset_name, import_year, value):
        self.asset_id = asset_id
        self.asset_name = asset_name
        self.import_year = import_year
        self.value = value

    def __str__(self):
        return f"{self.asset_id}\t{self.asset_name}"
