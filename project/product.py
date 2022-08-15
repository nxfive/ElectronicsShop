from project import database
import string


class Product:

    _pln_to_eur = 4.0
    _pln_to_usd = 4.6

    __trade_margin = 0.25

    def __init__(self, brand, prod_name, net_price=None, price_with_margin=None):
        Product._validate_input(brand, 'brand')
        self._brand = brand.capitalize()
        Product._validate_input(prod_name, 'prod_name')
        self._prod_name = prod_name.capitalize()
        self._net_price = net_price
        self._price_with_margin = price_with_margin

        if net_price:
            Product._validate_input(net_price, 'net_price')
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
        return f'Product: {self.__class__.__name__}\nBrand: {self.brand}, Name: {self.name}'

    @staticmethod
    def _validate_input(value, var_name):
        """The function checks data validation before creating an instance.
        If the entered data is correct, an instance of the class will be created."""
        if var_name == 'brand':
            if not isinstance(value, str):
                raise TypeError(f"The {var_name} value must be str. Not {type(value).__name__}.")
            if not value.isalpha():
                raise ValueError(f'The {var_name} value cannot include integers.')

        elif var_name == 'name':
            if not isinstance(value, str):
                raise TypeError(f"The {var_name} value must be str. Not {type(value).__name__}.")
            if not value.isalnum():
                raise ValueError(f"The {var_name} value should only include alpha-numeric chars.")

        elif var_name == 'net_price':
            if isinstance(value, (int, float)):
                if value < 0:
                    raise ValueError(f"The {var_name} value must be positive.")
            else:
                raise TypeError(f"The {var_name} must be int or float object. Not {type(value).__name__}.")

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
        Product._validate_input(value, 'brand')
        print("The brand changed.")
        self._brand = value.capitalize()

    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        Product._validate_input(value, 'prod_name')
        self._prod_name = value.capitalize()

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
        Product._validate_input(value, 'net_price')
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


if __name__ == '__main__':
    var = '123as'
    int(var)