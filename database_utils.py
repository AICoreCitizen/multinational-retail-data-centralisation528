# database_utils.py
import psycopg2

class DatabaseConnector:
    """A utility class for connecting to and uploading data to a PostgreSQL database."""

    def __init__(self, db_name, db_user, db_password, db_host="localhost", db_port=5432):
        # Initialize the database connection
        self.conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """Create a table in the database with the given name and columns."""
        # Create a SQL statement to create the table
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        # Execute the statement
        self.cursor.execute(sql)
        # Commit the changes
        self.conn.commit()

    def insert_data(self, table_name, data):
        """Insert data into a table in the database."""
        # Create a SQL statement to insert the data
        placeholders = ",".join(["%s"] * len(data[0]))
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        # Execute the statement for each row of data
        for row in data:
            self.cursor.execute(sql, row)
        # Commit the changes
        self.conn.commit()

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()