import sys

from pseudo_etl.pseudo_etl import PseudoETL
from utility.constant import PATH


if __name__ == "__main__":
    # Create object for the pseudo_etl class
    etl = PseudoETL(
        PATH.DB_INI_PATH,
        PATH.FILE_PATH,
        sys.argv[1],
        sys.argv[2]
    )
    # Run the application
    etl.run()
