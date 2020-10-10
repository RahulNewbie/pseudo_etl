import json


def read_json(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        print(data['data'])
        for item in data['data']:
            yield item


#for d in read_json(r"C:\Users\Rahul Dutta\PycharmProjects\test_etl\file.json"):
#    print(d)