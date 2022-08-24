import random

from project.person.customer import Customer
from project.utils.errors import NoSpaceError, ItemNotFoundError, ChangeContainerSizeError
from prettytable import PrettyTable
from project.person.worker import Worker
from project.utils.utils import input_validation as validate, create_product, create_worker
from project.product.laptop import Laptop
from project.product.phone import Phone


class Shop:

    _number_of_jobs = 5
    _sold_products_all = []

    def __init__(self, database,  name, max_capacity, amount_of_workers):
        self._database = database
        validate(name, 'name')
        self._name = name.capitalize()
        validate(max_capacity, 'max_capacity')
        self._max_capacity = max_capacity
        validate(amount_of_workers, 'amount_of_workers')
        self._amount_of_workers = amount_of_workers
        self._workers = self._create_workers()
        self._products = self._create_products()
        self._sold_products_by_instance = []

    @property
    def database(self):
        return self._database

    @property
    def products(self):
        return self._products

    @property
    def workers(self):
        return self._workers

    @property
    def amount_of_workers(self):
        return self._amount_of_workers

    @amount_of_workers.setter
    def amount_of_workers(self, value):
        validate(value, 'amount_of_workers')
        self._amount_of_workers = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        validate(value, 'name')
        self._name = value

    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        validate(value, 'max_capacity')
        self._max_capacity = value

    @property
    def sold_products_by_instance(self):
        return self._sold_products_by_instance

    @property
    def sold_products_all(self):
        return self._sold_products_all

    def show_max_capacity(self):
        print(f'Maximum shop capacity: {self.max_capacity}')

    def _create_workers(self):
        workers = []
        for _ in range(self.amount_of_workers):
            worker = Worker(self, *(create_worker()))
            workers.append(worker)
        return workers

    def _create_products(self):
        products = []
        for _ in range(self.max_capacity):
            class_choice = random.choice(('Phone', 'Laptop'))
            if class_choice == 'Phone':
                new_product = Phone(self, *(create_product('Phone')))
                products.append(new_product)
            else:
                new_product = Laptop(self, *(create_product('Laptop')))
                products.append(new_product)
        return products

    def add_product(self, amount):
        global i
        for i in range(amount):
            print(len(self.products))
            print(self.max_capacity)
            if len(self.products) < self.max_capacity:
                class_choice = random.choice(('Phone', 'Laptop'))
                if class_choice == 'Phone':
                    phone = Phone(self, *(create_product('Phone')))
                    self.products.append(phone)
                else:
                    laptop = Laptop(self, *(create_product('Laptop')))
                    self.products.append(laptop)
                print('Product has been added.')
            else:
                raise NoSpaceError(f'No space for another product. Added {i}/{amount} products.')

    def get_all_products_price(self):
        all_products_price = 0
        all_product_net_price = 0
        all_product_price_eur = 0
        all_product_price_usd = 0
        for product in self.products:
            if not product.__dict__ == {}:
                all_products_price += product.price_with_margin
                all_product_net_price += product.net_price
                all_product_price_eur += product._price_with_margin_eur
                all_product_price_usd += product._price_with_margin_usd
        print(f'PRICE OF ALL PRODUCTS IN >{self.name.upper()}<\n'
              f'>Net price:\n{all_product_net_price} PLN\n'
              f'>Price with margin:\n{all_products_price} PLN\n'
              f'{all_product_price_eur} EUR\n'
              f'{all_product_price_usd} USD\n')

    def get_amount_of_product_brand(self, product_brand):
        amount_brand = 0
        for product in self.products:
            if product.brand == product_brand:
                amount_brand += 1
        print(f'AMOUNT OF ALL PRODUCTS OF {product_brand.upper()} BRAND IN >{self.name.upper()}<\n>{amount_brand}')
        if amount_brand == 0:
            raise ItemNotFoundError(product_brand, f'We do not have {product_brand} in our shop.')

    def get_amount_of_product_name(self, product_name):
        amount_name = 0
        for product in self.products:
            if product.prod_name == product_name:
                amount_name += 1
        if amount_name == 0:
            raise ItemNotFoundError(product_name, f'We do not have {product_name} in our shop.')

    def get_list_of_all_products(self):
        # add sorted list by category and index from 1 to ...
        table_of_all_products = PrettyTable()
        table_of_all_products.title = f'LIST OF PRODUCTS IN {self.name.upper()}'
        table_of_all_products.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
        table_of_all_products.sortby = 'Category'
        for index, product in enumerate(self.products):
            table_of_all_products.add_row([index + 1, product.__class__.__name__, product.brand, product.prod_name,
                                          '{:.2f}'.format(product.price_with_margin)])
        print(table_of_all_products)
        Shop._get_specifics_of_products(self)

    def _get_specifics_of_products(self):
        print('Select product for more information.')
        try:
            choice = int(input(f'[1 - {len(self.products)}]: '))
            product = self.products[choice - 1]
            print(f"{product.__dict__}")
        except (ValueError, IndexError):
            print('Invalid input. Try again.')

    @staticmethod
    def display_list_of_customers():
        customers_table = PrettyTable()
        customers_table.title = 'LIST OF CUSTOMERS'
        customers_table.field_names = ['No.', 'Name', 'Surname', 'Items']
        for index, customer in enumerate(Customer.customers):
            customers_table.add_row([index+1, customer.name, customer.surname, customer.shopping_cart])
        print(customers_table)

    @staticmethod
    def display_list_of_workers():
        workers_table = PrettyTable()
        workers_table.title = "LIST OF WORKERS"
        workers_table.field_names = ['No.', 'Name', 'Surname', 'Position', 'Identity']
        for index, worker in enumerate(Worker.workers):
            workers_table.add_row([index+1, worker.name, worker.surname, worker.job_position, worker.identity])
        print(workers_table)

    @classmethod
    def change_number_of_jobs(cls, value):
        if isinstance(value, int) and value >= len(Worker.workers):
            Worker._number_of_jobs = value
        else:
            raise ChangeContainerSizeError(value, f'Cannot change the jobs to {value} place/s.')
