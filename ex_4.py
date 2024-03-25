import json
json_obj = '[["hvcvcj", 2],["cvcj", 4], ["hvcj", 3]]'
python_obj = json.loads(json_obj)
print(sorted(python_obj, key = lambda x: x[1], reverse=True))