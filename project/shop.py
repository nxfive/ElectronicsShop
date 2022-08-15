import random
from prettytable import PrettyTable
from laptop import Laptop
from phone import Phone
from worker import Worker
from project.utils import input_validation as validate


class Shop:

    def __init__(self, name, max_capacity, amount_of_workers):
        validate(name, 'name')
        self._name = name.capitalize()
        validate(max_capacity, 'max_capacity')
        self._max_capacity = max_capacity
        products = Shop._create_products(self)
        self.products = products
        validate(amount_of_workers, 'amount_of_workers')
        self._amount_of_workers = amount_of_workers
        self._workers = self._create_workers(amount_of_workers)

    @staticmethod
    def _create_workers(number):
        workers = []
        names = [name.rstrip() for name in open('../files/names.txt', encoding='UTF-8')]
        surnames = [surname.rstrip() for surname in open('../files/surnames.txt', encoding='UTF-8')]
        female_surnames = [surname for surname in surnames
                           if not surname.endswith(('ski', 'cki', 'sny', 'zki'))]

        male_surnames = [surname for surname in surnames
                         if not surname.endswith(('ska', 'cka', 'zka', 'sna'))]

        for _ in range(number):
            choice_name = random.choice(names)
            if choice_name.endswith('a'):
                choice_surname = random.choice(female_surnames)
                worker = Worker(choice_name, choice_surname)
                workers.append(worker)
            else:
                choice_surname = random.choice(male_surnames)
                worker = Worker(choice_name, choice_surname)
                workers.append(worker)

        return workers

    @staticmethod
    def _create_phone():
        brand = ['SamSam', 'Nova', 'Apl', 'Elgy']
        name_sa = ['se20 X', 'se21 Pro', 'se21 X', 'A 21i', 'A10x']
        name_no = ['No 1c', 'No', 'No 2x', 'Nok D12', 'Nok C0']
        name_ap = ['Pro Xd 11', 'Pro Xc 12', 'Pro Xc', 'Pro M1x']
        name_el = ['L1 Rex', 'L2 Pe', 'L23', 'L23 P', 'L X p']

        phone_brand = random.choice(brand)
        net_price = random.randint(2000, 5600)
        if phone_brand == 'SamSam':
            phone_name = random.choice(name_sa)
            p1 = Phone(phone_brand, phone_name, net_price)
            return p1

        if phone_brand == 'Nova':
            phone_name = random.choice(name_no)
            p1 = Phone(phone_brand, phone_name, net_price)
            return p1

        if phone_brand == 'Apl':
            phone_name = random.choice(name_ap)
            p1 = Phone(phone_brand, phone_name, net_price)
            return p1

        if phone_brand == 'Elgy':
            phone_name = random.choice(name_el)
            p1 = Phone(phone_brand, phone_name, net_price)
            return p1

    @staticmethod
    def _create_laptop():
        brand = ['Eycer', 'Aply', 'Hapec', 'Leno']
        name_ey = ['MT1', 'MT200', 'Max Prof1', 'MaxProf2']
        name_len = ['Gamer One', 'Gamer X', 'Ideal200', 'IdealX', 'Nest Pro']
        name_hap = ['Fusion P', 'FX One', 'FX Two', 'Fusion Pro']
        name_apl = ['Pro 10', 'Pro 11', 'Pro 12', 'Max PX', 'Max X4']

        lap_brand = random.choice(brand)
        net_price = random.randint(2200, 4800)

        if lap_brand == 'Eycer':
            lap_name = random.choice(name_ey)
            l1 = Laptop(lap_brand, lap_name, net_price)
            return l1

        if lap_brand == 'Aply':
            lap_name = random.choice(name_apl)
            l1 = Laptop(lap_brand, lap_name, net_price)
            return l1

        if lap_brand == 'Hapec':
            lap_name = random.choice(name_hap)
            l1 = Laptop(lap_brand, lap_name, net_price)
            return l1

        if lap_brand == 'Leno':
            lap_name = random.choice(name_len)
            l1 = Laptop(lap_brand, lap_name, net_price)
            return l1

    def _create_products(self):
        products = []
        for i in range(self.max_capacity):
            new_product = random.choice([Shop._create_laptop(), Shop._create_phone()])
            products.append(new_product)
        return products

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
            print(f'Product {product.brand} {product.name} has been added.')
        else:
            print('The shop is full.')

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
            if product.brand == product_brand.capitalize():
                amount_brand += 1
        print(f'AMOUNT OF ALL PRODUCTS OF {product_brand.upper()} BRAND IN >{self.name.upper()}<\n>{amount_brand}')
        if amount_brand == 0:
            print(f'We do not have {product_brand} in our shop.')

    def get_amount_of_product_name(self, product_name):
        '''self -> shop.
           product_name -> str, name of product'''
        amount_name = 0
        product_brand = ''
        for product in self.products:
            if product.name == product_name.capitalize():
                amount_name += 1
                if not product_brand:
                    product_brand += product.brand
        print(f'AMOUNT OF {product_name} IN >{self.name.upper()}<\n>{amount_name}')

    def get_list_of_all_products(self):
        # add sorted list by category and index from 1 to ...
        table_of_all_products = PrettyTable()
        table_of_all_products.title = f'LIST OF PRODUCTS IN {self.name.upper()}'
        table_of_all_products.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
        table_of_all_products.sortby = 'Category'
        table_of_all_products.sortby = 'No.'
        for index, product in enumerate(self.products):
            if not product.__dict__ == {}:
                table_of_all_products.add_row([index+1, product.__class__.__name__, product.brand, product.name,
                                               '{:.2f}'.format(product.price_with_margin)])
        print(table_of_all_products)
        Shop._get_specifics_of_products(self)

    def _get_specifics_of_products(self):
        print('Select product for more information.')
        try:
            choice = int(input(f'[1 - {len(self.products)}]: '))
            product = self.products[choice - 1]
            print(product)          # {product}: __str__ format
        except (ValueError, IndexError):
            print('Invalid input. Try again.')
