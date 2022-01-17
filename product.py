class Product:
    _pln_to_eur = 4.0
    _pln_to_usd = 4.6

    __trade_margin = 0.25

    def __init__(self, brand, name, net_price=None, price_with_margin=None):
        Product._validate_input(brand, 'brand')
        self._brand = brand.capitalize()
        Product._validate_input(name, 'name')
        self._name = name.capitalize()
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

        elif var_name == 'net_price':
            if not isinstance(value, (int, float)):
                raise TypeError(f"The {var_name} value must be int or float object. Not {type(value).__name__}.")
            if value < 0:
                raise ValueError(f"The {var_name} value must be positive.")

    def _validate_value(self, value, var_name):
        """The function checks validations for data that will be overwritten for the specified instance."""
        if var_name == 'brand':
            if isinstance(value, str):
                if not value.isalpha():
                    raise ValueError(f'The {var_name} value cannot include integers.')
            else:
                raise TypeError(f"The {var_name} must be str. Not {type(value).__name__}.")

        elif var_name == 'name':
            if isinstance(value, (int, float)):
                raise TypeError(f"The {var_name} value must be str. Not {type(value).__name__}.")

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
        Product._validate_value(self, value, 'brand')
        print("The brand changed.")
        self._brand = value.capitalize()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Product._validate_value(self, value, 'name')
        self._name = value.capitalize()

    @name.deleter
    def name(self):
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
        answer = input(f'Do you want to change the net price of {self.name} product [y/n]: ')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            Product._validate_value(self, value, 'net_price')
            print("Validation setting price complete.")
            self._net_price = value
            # at first I delete the price with margin
            # that was related to the previous net_price
            self._price_with_margin = None
            print("Price with margin deleted.")
            # now I set the new price with margin from new net_price
            Product._convert_price_with_margin(self)
        else:
            print(f'Net price is still: {self.net_price}.')

    @net_price.deleter
    def net_price(self):
        print("Deleting...")
        for attr in list(self.__dict__.keys()):
            if attr.startswith('_price') or attr.startswith('_net'):
                delattr(self, attr)

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
