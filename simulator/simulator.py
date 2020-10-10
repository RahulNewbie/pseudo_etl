import random
import datetime
import time
import string
import json


def id_generator(
        size=4,
        chars=string.ascii_uppercase + string.digits
):
    return ''.join(random.choice(chars) for _ in range(size))


def value_generator():
    return random.uniform(10.0, 100.0)


def time_stamp_generator():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


def data_generator():
    data = {
        'key': id_generator(),
        'value': value_generator(),
        'ts': time_stamp_generator()
        }
    return json.dumps(data)


