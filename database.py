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


db = Database('shopdata.db')


def create_database():
    global db

    db.create_table('Workers', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, '
                    'identity INTEGER, job_position TEXT')

    db.create_table('Customers', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, '
                    'entry_time REAL, exit_time REAL')

    db.create_table('Products', 'id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, brand TEXT, '
                    'name TEXT, net_price REAL, price_with_margin REAL')


def insert_data(obj_instance, database_instance, name_table: str):
    if name_table == 'Workers':
        database_instance.insert_data(name_table, None, obj_instance.name, obj_instance.surname,
                                      obj_instance.identity, obj_instance.job_position)

    if name_table == 'Customers':
        database_instance.insert_data(name_table, None, obj_instance.name, obj_instance.surname,
                                      obj_instance.entry_time, obj_instance.exit_time)

    if name_table == 'Products':
        database_instance.insert_data(name_table, None, obj_instance.__class__.__name__,
                                      obj_instance.brand, obj_instance.name, obj_instance.net_price,
                                      obj_instance.price_with_margin)


create_database()
