import uuid
from project.database.database import *
from project.utils.utils import input_validation as validate


class Product:

    _pln_to_eur = 4.0
    _pln_to_usd = 4.6

    _trade_margin = 0.25

    def __init__(self, brand, prod_name, net_price=None, price_with_margin=None):
        self.identity = uuid.uuid4().fields[-1]
        validate(brand, 'brand')
        self._brand = brand
        validate(prod_name, 'prod_name')
        self._prod_name = prod_name
        self._net_price = net_price
        self._price_with_margin = price_with_margin

        if net_price:
            validate(net_price, 'net_price')
            self._net_price = net_price

            Product._convert_price_with_margin(self)
            Product._convert_price_with_margin_to_usd(self)
            Product._convert_price_with_margin_to_eur(self)
        else:
            self._price_with_margin = None
            self._price_with_margin_eur = None
            self._price_with_margin_usd = None
        insert_data(self, database, 'products')

    def __del__(self):
        print('deleted')

    def __str__(self):
        return f'[{self.__class__.__name__}] brand: {self.brand}, prod_name: {self.prod_name}'

    def __repr__(self):
        return f'{self.__class__.__name__}=(brand: {self.brand}, prod_name: {self.prod_name})'

    def _convert_price_with_margin(self):
        if self.net_price:
            self._price_with_margin = self.net_price * (1 + Product._trade_margin)
            return self._price_with_margin
        else:
            print("There is no value assigned to the product price.")

    def _convert_price_with_margin_to_eur(self):
        if self.price_with_margin:
            self._price_with_margin_eur = round((self.price_with_margin / Product._pln_to_eur), 2)

    def _convert_price_with_margin_to_usd(self):
        if self.price_with_margin:
            self._price_with_margin_usd = round((self.price_with_margin / Product._pln_to_usd), 2)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        validate(value, 'brand')
        self._brand = value

    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        validate(value, 'prod_name')
        self._prod_name = value

    @property
    def net_price(self):
        return self._net_price

    @net_price.setter
    def net_price(self, value):
        validate(value, 'net_price')
        self._net_price = value
        self._price_with_margin = None
        Product._convert_price_with_margin(self)
        Product._convert_price_with_margin_to_eur(self)
        Product._convert_price_with_margin_to_usd(self)

    @net_price.deleter
    def net_price(self):
        print("Deleting...")
        for attr in list(self.__dict__.keys()):
            if attr.startswith('_price') or attr.startswith('_net'):
                setattr(self, attr, None)

    @property
    def trade_margin(self):
        return self._trade_margin

    @trade_margin.setter
    def trade_margin(self, value):
        if isinstance(value, float):
            if 0 <= value < 1:
                self._trade_margin = value
            else:
                raise ValueError('Trade margin must be between 0 and 1.')
        else:
            raise TypeError(f'Trade margin must be float type. Not {type(value).__name__}.')

    @property
    def price_with_margin(self):
        return self._price_with_margin
