import json

with open("C:\\Users\\lenovo\\Desktop\\Files\\example_2.json","r") as f_json:
    json_data=f_json.read()


py_dict=json.loads(json_data)
print(type(py_dict["quiz"]))
for data in py_dict["quiz"]:
    print('type is ',type(data))
    #del py_dict["quiz"][data]
    for k in py_dict["quiz"][data]["q1"]:
        if k == 'options':
            del py_dict["quiz"][data]["q1"][k]
print(py_dict)

with open("C:\\Users\\lenovo\\Desktop\\Files\\example_2_q1_options_del.json", "w") as outfile:
    json.dump(py_dict, outfile, indent = 4)


    #for k in py_dict["quiz"][data]["q1"]:
    #    del k["question"]