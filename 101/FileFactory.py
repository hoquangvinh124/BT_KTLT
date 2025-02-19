import json
import os

class FileFactory:
    def write_data(self, path, arr_data):
        json_string = json.dumps([item.__dict__ for item in arr_data], default=str)
        with open(path, "w") as json_file:
            json_file.write(json_string)

    def read_data(self, path, class_name):
        if not os.path.isfile(path):
            return []
        with open(path, "r") as file:
            arr_data = json.loads(file.read(), object_hook=lambda d: class_name(**d))
        return arr_data
