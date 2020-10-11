import json


def read_json(file_path):
    """ read json array file and return single json
        to insert row in database
    """
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            for json_item in data['data']:
                # Generator to send single json
                yield json_item
    except (Exception, OSError) as error:
        print(error)
