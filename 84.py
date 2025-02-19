import json
python_object = {
 "Name": "Hồ Quang Vinh",
 "Age": 20,
 "Id": "US1"
}
json_string = json.dumps(python_object, ensure_ascii=False)
print(json_string)