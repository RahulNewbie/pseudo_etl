import os


class SourceMode:
    SIMULATOR = "simulator"
    FILE = "file"


class SinkMode:
    CONSOLE = "console"
    DATABASE = "database"


class PATH:
    DB_INI_PATH = str(os.getcwd()) + "/database.ini"
    FILE_PATH = str(os.getcwd()) + "/file.json"

