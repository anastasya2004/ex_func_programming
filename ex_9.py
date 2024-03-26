import json
import xmltodict
import yaml

def to_format(f=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            
            if f == 'json' or f is None:
                return json.dumps(result)
            elif f == 'xml':
                xml_to_dict = xmltodict.parse(result)
                return json.dumps(xml_to_dict)
            elif f == 'yaml':
                return yaml.dump(result)
        
        return wrapper
    return decorator

@to_format()
def get_dict():
    return {"name": "Nasty", "age": 19,"city": "Novosibirsk"}

print(get_dict()) 

@to_format('xml')
def get_tuple():
    return (10, 5), (2, 9), (0, 4)

print(get_tuple()) 

@to_format('yaml')
def get_list():
    return ['Monday', 'Tuesday ', 'Wednesday', 'Thursday ', 'Friday', 'Saturday', 'Sunday']

print(get_list()) 

