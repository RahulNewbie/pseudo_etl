import random
import datetime
import string
import json


def _id_generator(
        size=4,
        chars=string.ascii_uppercase + string.digits
):
    """ Generate id for the data
    """
    return ''.join(random.choice(chars) for _ in range(size))


def _value_generator():
    """ Generate value for the data
    """
    return random.uniform(10.0, 100.0)


def _time_stamp_generator():
    """ Generate timestamp for the data
    """
    return datetime.datetime.now(datetime.timezone.utc).\
        strftime('%Y-%m-%d %H:%M:%S.%f %z')


def data_generator():
    """ Generate simulated ETL data
    """
    data = {
        'key': _id_generator(),
        'value': _value_generator(),
        'ts': _time_stamp_generator()
        }
    return json.dumps(data)


