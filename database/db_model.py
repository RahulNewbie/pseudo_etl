import psycopg2


class DbModel(object):
    """ DbModel
        Takes care of storing and loading data structures
        to PostgreSQL database
    """
    def __init__(self, configuration):
        self.config = configuration
        self.connection = None
        self._prepare_connection()
        self._create_table()

    def __del__(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def __enter__(self):
        self._prepare_connection()
        self._create_table()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        self.connection = None

    def _prepare_connection(self):
        """ Creates a new connection if it was not
            created yet or was closed
        """
        try:
            if self.connection is None or self.connection.closed:
                self.connection = psycopg2.connect(**self.config)
            print("Database connected successfully........")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def _create_table(self):
        """ Creates a new table if table doesn't exists
        """
        try:
            # Creating a cursor object using the cursor() method
            cursor = self.connection.cursor()

            # Creating table as per requirement
            sql = '''CREATE TABLE IF NOT EXISTS ETL(
                key VARCHAR(255) PRIMARY KEY,
                value VARCHAR(255) NOT NULL,
                timestamp VARCHAR(255) NOT NULL
            )'''
            cursor.execute(sql)
            print("Table created successfully........")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def insert_data(self, data):
        """ Inserts a record in the database
        """
        try:
            # Creating a cursor object using the cursor() method
            cursor = self.connection.cursor()

            # Preparing SQL queries to INSERT a record into the database.
            cursor.execute('''INSERT INTO ETL(key, value, timestamp) 
            VALUES (%s,%s,%s)''', (data['key'], data['value'], data['ts'],))
            # Commit your changes in the database
            self.connection.commit()
            print("Records inserted........")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
