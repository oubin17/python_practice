import json

data = {
    'a': 1,
    "b": 'asg'
}
json_data = json.dumps(data)
json_data2 = json.loads(json_data)
print(json_data2)