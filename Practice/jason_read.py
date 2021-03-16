import json

with open("C:\\Users\\lenovo\\Desktop\\Files\\example_2.json","r") as f_json:
    json_data=f_json.read()


py_dict=json.loads(json_data)
print(py_dict)
print(json.dumps(py_dict, indent = 4))

with open("C:\\Users\\lenovo\\Desktop\\Files\\example_2_conv.json", "w") as outfile:
    json.dump(py_dict, outfile, indent = 4)