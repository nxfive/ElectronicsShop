import random
from prettytable import PrettyTable
from laptop import Laptop
from phone import Phone


class Shop:

    def __init__(self, name, max_capacity):
        Shop._input_validation(name, 'name')
        self._name = name.capitalize()
        Shop._input_validation(max_capacity, 'max_capacity')
        self._max_capacity = max_capacity
        products = Shop.create_products(self)
        self.products = products

    @staticmethod
    def create_phone():
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
    def create_laptop():
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

    def create_products(self):
        products = []
        for i in range(self.max_capacity):
            new_product = random.choice([Shop.create_laptop(), Shop.create_phone()])
            products.append(new_product)
        return products

    @staticmethod
    def _input_validation(value, var_name):
        if var_name == 'name':
            if not isinstance(value, str):
                raise TypeError(f'Name of the shop must be a str object. Not {type(value).__name__}.')
            if not len(value) >= 3:
                raise ValueError(f'Length name of the shop must be equal or greater than 3.')
            if not value.isalpha():
                raise ValueError('Name of the shop cannot include integers.')

        elif var_name == 'max_capacity':
            if not isinstance(value, int):
                raise TypeError(f'Value of the maximum capacity must be an int object. Not {type(value).__name__}.')
            if value < 0:
                raise ValueError('Value of the maximum capacity must be greater than zero!')

    def _value_validation(self, value, var_name):
        if var_name == 'name':
            if not isinstance(value, str):
                raise TypeError(f'Name of the shop must be a str object. Not {type(value).__name__}.')
            if not len(value) >= 3:
                raise ValueError(f'Length name of the shop must be equal or greater than 3.')
            if not value.isalpha():
                raise ValueError('Name of the shop cannot include integers.')
            self._name = value.capitalize()

        elif var_name == 'max_capacity':
            if not isinstance(value, int):
                raise TypeError(f'Value of the maximum capacity must be an int object. Not {type(value).__name__}.')
            if value < 0:
                raise ValueError('Value of the maximum capacity must be greater than zero!')
            self._max_capacity = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Shop._value_validation(self, value, 'name')

    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value):
        Shop._value_validation(self, value, 'max_capacity')

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
        table_of_all_products = PrettyTable()
        table_of_all_products.title = f'LIST OF PRODUCTS IN {self.name.upper()}'
        table_of_all_products.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
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
