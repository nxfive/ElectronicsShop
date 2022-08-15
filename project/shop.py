import random
from project.errors import NoSpaceError, ItemNotFoundError
from prettytable import PrettyTable
from project.worker import Worker
from project.utils import input_validation as validate, create_product, create_worker
from project.laptop import Laptop
from project.phone import Phone


class Shop:

    def __init__(self, name, max_capacity, amount_of_workers):
        validate(name, 'name')
        self._name = name.capitalize()
        validate(max_capacity, 'max_capacity')
        self._max_capacity = max_capacity
        validate(amount_of_workers, 'amount_of_workers')
        self._amount_of_workers = amount_of_workers
        self._workers = self._create_workers()
        self._products = self._create_products()

    def _create_workers(self):
        workers = []
        for i in range(self.amount_of_workers):
            worker = Worker(*(create_worker()))
            workers.append(worker)
        return workers

    def _create_products(self):
        products = []
        for i in range(self.max_capacity):
            class_choice = random.choice(('Phone', 'Laptop'))
            if class_choice == 'Phone':
                new_product = Phone(*(create_product('Phone')))
                products.append(new_product)
            else:
                new_product = Laptop(*(create_product('Laptop')))
                products.append(new_product)
        return products

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

    def show_max_capacity(self):
        print(f'Maximum shop capacity: {self.max_capacity}')

    def add_product(self, product):
        if len(self.products) < self._max_capacity:
            self.products.append(product)
            print('Product has been added.')
        else:
            raise NoSpaceError(product, f'No space for `{product.prod_name}` product.')

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
        '''self -> shop.
           product_name -> str, name of product'''
        amount_name = 0
        product_brand = ''
        for product in self.products:
            if product.prod_name == product_name.capitalize():
                amount_name += 1
                if not product_brand:
                    product_brand += product.brand
        if amount_name == 0:
            raise ItemNotFoundError(product_name, f'We do not have {product_name} in our shop.')

    def get_list_of_all_products(self):
        # add sorted list by category and index from 1 to ...
        table_of_all_products = PrettyTable()
        table_of_all_products.title = f'LIST OF PRODUCTS IN {self.name.upper()}'
        table_of_all_products.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
        table_of_all_products.sortby = 'Category'
        table_of_all_products.sortby = 'No.'
        for index, product in enumerate(self.products):
            if not product.__dict__ == {}:
                table_of_all_products.add_row([index + 1, product.__class__.__name__, product.brand, product.prod_name,
                                               '{:.2f}'.format(product.price_with_margin)])
        print(table_of_all_products)
        Shop._get_specifics_of_products(self)

    def _get_specifics_of_products(self):
        print('Select product for more information.')
        try:
            choice = int(input(f'[1 - {len(self.products)}]: '))
            product = self.products[choice - 1]
            print(product)  # {product}: __str__ format
        except (ValueError, IndexError):
            print('Invalid input. Try again.')
