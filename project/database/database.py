import sqlite3


class Database:

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def create_table(self, table_name, values):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}({values})''')
        self.connection.commit()

    def insert(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(['?' for _ in values])})", values)
        self.connection.commit()

    def delete_one(self, table_name, identity):
        self.cursor.execute(f"DELETE from {table_name} WHERE identity=(?)", identity)
        self.connection.commit()

    def show_all(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        self.connection.commit()

    def update_customer(self, table_name, instance):
        self.cursor.execute(f"UPDATE {table_name} SET bill = '{instance._bill}', exit_time = '{instance._exit_time}' "
                            f"WHERE identity = {instance.identity}")
        self.connection.commit()

    def update_product(self, table_name, identity):
        self.cursor.execute(f"UPDATE {table_name} SET status = 'sold' WHERE identity = {identity}")
        self.connection.commit()


database = Database('shopdata.db')


def create_database():
    global database

    database.create_table('workers', 'identity INTEGER, name TEXT, surname TEXT, job_position TEXT')

    database.create_table('customers', 'identity INTEGER, name TEXT, surname TEXT, email TEXT, '
                                       'city TEXT, bill REAL, entry_time REAL, exit_time REAL')

    database.create_table('products', 'identity INTEGER, category TEXT, brand TEXT, prod_name TEXT, net_price REAL, '
                                      'price_with_margin REAL, status TEXT')

    database.create_table('sold', 'identity INTEGER, category TEXT, brand TEXT, prod_name TEXT, net_price REAL, '
                                  'price_with_margin REAL, profit REAL')


def insert_data(obj_instance, database_instance, table_name: str):
    if table_name == 'workers':
        database_instance.insert(table_name, (obj_instance.identity, obj_instance.name, obj_instance.surname,
                                              obj_instance.job_position))

    if table_name == 'customers':
        database_instance.insert(table_name, (obj_instance.identity, obj_instance.name, obj_instance.surname,
                                              obj_instance.email, obj_instance.city, obj_instance._bill,
                                              obj_instance.entry_time, obj_instance._exit_time))

    if table_name == 'products':
        database_instance.insert(table_name, (obj_instance.identity, obj_instance.__class__.__name__,
                                              obj_instance.brand, obj_instance.prod_name, obj_instance.net_price,
                                              obj_instance.price_with_margin, 'in stock'))

    if table_name == 'sold':
        database_instance.insert(table_name, (obj_instance.identity, obj_instance.__class__.__name__,
                                              obj_instance.brand, obj_instance.prod_name, obj_instance.net_price,
                                              obj_instance.price_with_margin,
                                              obj_instance.price_with_margin - obj_instance.net_price))


create_database()
