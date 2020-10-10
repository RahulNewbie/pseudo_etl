from pseudo_etl.pseudo_etl import PseudoETL
from utility.constant import SourceMode, SinkMode, PATH


if __name__ == "__main__":
    etl = PseudoETL(
        PATH.DB_INI_PATH,
        PATH.FILE_PATH
    )
    # Source is simulator and Sink is Console
    etl.run(
        SourceMode.SIMULATOR,
        SinkMode.CONSOLE
    )
    # Source is simulator and Sink is Database
    etl.run(
        SourceMode.SIMULATOR,
        SinkMode.DATABASE
    )
    # Source is File and Sink is Database
    etl.run(
        SourceMode.FILE,
        SinkMode.DATABASE
    )

