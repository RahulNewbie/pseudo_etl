import json


def read_json(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            for item in data['data']:
                yield item
    except (Exception, OSError) as error:
        print(error)
