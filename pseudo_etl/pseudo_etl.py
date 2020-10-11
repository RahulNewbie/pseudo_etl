import json

from simulator.simulator import data_generator
from database.db_model import DbModel
from database.config import config
from file.file_reader import read_json
from utility.constant import SinkMode, SourceMode


class PseudoETL:
    """ Pseudo ETL class, responsible for source the data
        and sink it to database/ console
    """
    def __init__(self, ini_path, file_path, source, sink):
        self.database = DbModel(config(ini_path))
        self.data = None
        self.file_path = file_path
        self.source = source
        self.sink = sink

    def start_sink(self):
        """ Responsible to sink the data into console/ database
        """
        try:
            if self.sink == SinkMode.CONSOLE:
                if self.data is not None:
                    # Print the data in console
                    print("Record is {}".format(self.data))
            if self.sink == SinkMode.DATABASE:
                if self.data is not None:
                    # Insert the data in Postgresql
                    self.database.insert_data(self.data)

        except (Exception, OSError) as error:
            print(error)

    def start_source(self):
        """ Responsible to source the data using simulator/file
        """
        try:
            if self.source == SourceMode.SIMULATOR:
                # Simulate data to sink
                self.data = json.loads(data_generator())
                self.start_sink()
            if self.source == SourceMode.FILE:
                # Read the file and sink
                for json_data in read_json(self.file_path):
                    self.data = json_data
                    self.start_sink()
        except (Exception, OSError) as error:
            print(error)

    def run(self):
        """ Responsible for running the Pseudo ETL workflow
        """
        self.start_source()
