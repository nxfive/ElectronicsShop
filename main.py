from database import Database
from worker import Worker
from customer import Customer
from shop import Shop
from laptop import Laptop
from phone import Phone


def create_and_add_to_database():
    db = Database('shopdata.db')

    db.create_table('Workers', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, '
                    'identity INTEGER, job_position TEXT')

    db.create_table('Customers', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, '
                    'entry_time REAL, exit_time REAL')

    db.create_table('Products', 'id INTEGER PRIMARY KEY AUTOINCREMENT, class TEXT, brand TEXT, '
                    'name TEXT, net_price REAL, price_with_margin REAL')

    w1 = Worker(name='Marcin', surname='Kowalski')
    w2 = Worker(name='Damian', surname='Kałuża')
    c1 = Customer(name='Piotr', surname='Nowak')
    c2 = Customer(name='Kasia', surname='Maklowicz')
    l1 = Laptop(brand='Leno', name='LD12', net_price=3000)
    l2 = Laptop(brand='HaP', name='Sface123', net_price=3400)

    db.insert_data('Workers', None, w1.name, w1.surname, w1.identity, w1.job_position)
    db.insert_data('Workers', None, w2.name, w2.surname, w2.identity, w2.job_position)
    db.insert_data('Customers', None, c1.name, c1.surname, c1.entry_time, c1.exit_time)
    db.insert_data('Customers', None, c2.name, c2.surname, c2.entry_time, c2.exit_time)
    db.insert_data('Products', None, l1.__class__.__name__, l1.brand, l1.name, l1.net_price, l1.price_with_margin)
    db.insert_data('Products', None, l2.__class__.__name__, l2.brand, l2.name, l2.net_price, l2.price_with_margin)


def main():
    # create Shop
    shop = Shop('ElectronicShop', 5)

    # show max capacity
    shop.show_max_capacity()

    # create products
    laptop1 = Laptop('Leno', 'NT45', 4500)
    laptop2 = Laptop('Hpe', 'Mx123', 3450)

    phone1 = Phone('Telcom', 'A34', 3109)
    phone2 = Phone('Telxcom', 'X23', 5300)


    # add products to the shop
    shop.add_product(laptop1)
    shop.add_product(laptop2)

    shop.add_product(phone1)
    shop.add_product(phone2)


    # add informations of the products
    laptop1.ram_memory = 64
    laptop1.built_in_memory = 512
    # you can set type in lowercase
    laptop1.type_drive = 'ssd'

    laptop2.ram_memory = 8
    laptop2.built_in_memory = 128
    laptop2.type_drive = 'SSHD'

    phone1.is_camera = True
    phone1.is_keyboard = True
    phone1.is_touch_screen = False
    phone1.memory = 64

    phone2.is_camera = True
    phone2.is_keyboard = False
    phone2.is_touch_screen = True
    phone2.memory = 512

    # show price of the all products in the shop
    shop.get_all_products_price()

    # show amount of product brand
    shop.get_amount_of_product_brand('Leno')

    # show amount of the product name
    shop.get_amount_of_product_name('NT45')

    # show list of the all products
    shop.get_list_of_all_products()

    # show specifics of the products
    shop.get_specifics_of_products()

    # create workers
    w1 = Worker(name='Marcin', surname='Kowalski')
    w2 = Worker(name='Damian', surname='Kałuża')

    # add workers to list of employees
    w1.add_worker_to_list()
    w2.add_worker_to_list()

    # show list of workers
    Worker.display_list_of_workers()

    # create customer
    c1 = Customer(name='Piotr', surname='Nowak')
    # c2 = Customer(name='Kasia', surname='Maklowicz')

    # add customer to the list of all customers
    c1.add_customer_to_list()

    # show list of customers
    Customer.display_list_of_customers()

    # add products to shopping cart
    c1.add_to_shopping_cart('X23', shop)
    c1.add_to_shopping_cart('A34', shop)

    # show added products
    c1.list_shopping_cart()

    # delete product from shopping cart
    c1.del_from_shopping_cart('A34')
    c1.list_shopping_cart()

    c1.paid_for_items()
    c1.bye()
    print(c1.__dict__)


if __name__ == '__main__':
    main()
