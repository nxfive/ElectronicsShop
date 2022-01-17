import sqlite3


class Database:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table_name, values):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}({values})''')
        self.connection.commit()

    def insert_data(self, table_name, *values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()