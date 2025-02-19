import json

json_string = '{ "Id":"1", "Age":20, "Name":"Hồ Quang Vinh"}'
data_object = json.loads(json_string)
print(data_object)
print("ID =",data_object["Id"])
print("Age =",data_object["Age"])
print("Name =",data_object["Name"])