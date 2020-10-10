import json

from simulator.simulator import data_generator
from database.db_model import DbModel
from database.config import config
from file.file_reader import read_json


class PseudoETL:
    def __init__(self, ini_path, file_path):
        self.database = DbModel(config(ini_path))
        self.data = None
        self.file_path = file_path

    def sink(self, sink):
        if sink == "console":
            if self.data is not None:
                print(self.data)
        if sink == "database":
            self.database.insert_data(
                self.data['key'],
                self.data['value'],
                self.data['ts']
            )

    def run(self, source, sink):
        if source == "simulator":
            self.data = json.loads(data_generator())
            self.sink(sink)
        if source == "file":
            for json_data in read_json(self.file_path):
                self.data = json_data
                print(self.data)
                self.sink(sink)
