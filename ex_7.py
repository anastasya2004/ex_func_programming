import json
def to_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapper

@to_json
def get_num():
    return 25

print(get_num()) 

@to_json
def get_str():
    return 'python code'

print(get_str()) 

@to_json
def get_dict():
    return {"name": "Nasty", "age": 19,"city": "Novosibirsk"}

print(get_dict()) 

@to_json
def get_tuple():
    return (10, 5), (2, 9), (0, 4)

print(get_tuple()) 

@to_json
def get_list():
    return ['Monday', 'Tuesday ', 'Wednesday', 'Thursday ', 'Friday', 'Saturday', 'Sunday']

print(get_list()) 



