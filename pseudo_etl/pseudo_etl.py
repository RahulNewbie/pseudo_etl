import json

from simulator.simulator import data_generator
from database.db_model import DbModel
from database.config import config
from file.file_reader import read_json
from utility.constant import SinkMode, SourceMode


class PseudoETL:
    def __init__(self, ini_path, file_path, source, sink):
        self.database = DbModel(config(ini_path))
        self.data = None
        self.file_path = file_path
        self.source = source
        self.sink = sink

    def start_sink(self):
        try:
            if self.sink == SinkMode.CONSOLE:
                if self.data is not None:
                    print(self.data)
            if self.sink == SinkMode.DATABASE:
                if self.data is not None:
                    self.database.insert_data(self.data)

        except (Exception, OSError) as error:
            print(error)

    def start_source(self):
        try:
            if self.source == SourceMode.SIMULATOR:
                self.data = json.loads(data_generator())
                self.start_sink()
            if self.source == SourceMode.FILE:
                for json_data in read_json(self.file_path):
                    self.data = json_data
                    self.start_sink()
        except (Exception, OSError) as error:
            print(error)

    def run(self):
        self.start_source()
