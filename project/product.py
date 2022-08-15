from project import database
from project.utils import input_validation as validate


class Product:

    _pln_to_eur = 4.0
    _pln_to_usd = 4.6

    __trade_margin = 0.25

    def __init__(self, brand, prod_name, net_price=None, price_with_margin=None):
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
        database.insert_data(self, database.db, 'Products')

    def __str__(self):
        return f'Class: {self.__class__.__name__}, brand: {self.brand}, name: {self.prod_name}'

    def _convert_price_with_margin(self):
        if self.net_price:
            self._price_with_margin = self.net_price * (1 + Product.__trade_margin)
            return self._price_with_margin
        else:
            print("There is no value assigned to the product price.")

    def _convert_price_with_margin_to_eur(self):
        # print("Setting price with margin in EUR...")
        if self.price_with_margin:
            self._price_with_margin_eur = round((self.price_with_margin / Product._pln_to_eur), 2)
            # print("Successfully converted amount to EUR.")

    def _convert_price_with_margin_to_usd(self):
        # print("Setting price with margin in USD...")
        if self.price_with_margin:
            self._price_with_margin_usd = round((self.price_with_margin / Product._pln_to_usd), 2)
            # print("Successfully converted amount to USD.")

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

    @prod_name.deleter
    def prod_name(self):
        """If you delete a name of object you also
           delete the rest of the attributes. Object will
           still exist like an empty dict {}."""
        for attr in list(self.__dict__.keys()):
            delattr(self, attr)

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
        return Product.__trade_margin

    @trade_margin.setter
    def trade_margin(self, value):
        if isinstance(value, float):
            if 0 <= value < 1:
                Product.__trade_margin = value
        else:
            raise TypeError(f'Trade margin must be a float object. Not {type(value).__name__}.')

    @property
    def price_with_margin(self):
        return self._price_with_margin
