from product import Product


class Laptop(Product):

    def __init__(self, brand, name, net_price, ram_memory=None, built_in_memory=None, type_drive=None):
        super().__init__(brand, name, net_price)
        if ram_memory:
            Laptop._validate_input(ram_memory, 'ram_memory')
            self._ram_memory = ram_memory
        else:
            self._ram_memory = None

        if built_in_memory:
            Laptop._validate_input(built_in_memory, 'built_in_memory')
            self._built_in_memory = built_in_memory
        else:
            self._built_in_memory = None

        if type_drive:
            Laptop._validate_input(type_drive, 'type_drive')
            self._type_drive = type_drive
        else:
            self._type_drive = None

    def __str__(self):
        return f'{super().__str__()}, Price: {self.price_with_margin}\nRAM memory: {self.ram_memory}\n' \
               f'Built-in memory: {self.built_in_memory}\nType of drive: {self.type_drive}'

    @staticmethod
    def _validate_input(value, var_name):
        if var_name == 'ram_memory' or var_name == 'built_in_memory':
            if not isinstance(value, int):
                raise TypeError(f"{var_name.capitalize().replace('_', ' ')} "
                                f"must be int object. Not {type(value).__name__}.")
        elif var_name == 'ram_memory':
            if value not in [4, 8, 16, 64]:
                raise ValueError('Ram memory value must be in [4, 8, 16, 64].')

        elif var_name == 'built_in_memory':
            if value not in [128, 256, 512, 1024]:
                raise ValueError('Built in memory value must be in [128, 256, 512, 1024].')

        elif var_name == 'type_drive':
            if not isinstance(value, str):
                raise TypeError(f'Type of Hard Drive must be str object. Not {type(value).__name__}.')
            types = ['SSD', 'SSHD', 'HDD']
            if value not in types:
                raise ValueError(f'Wrong value entered. Check your input. It cant be {type(value).__name__}.')

    def _validate_value(self, value, var_name):
        if var_name == 'ram_memory':
            if not isinstance(value, int):
                raise TypeError(f"{var_name.capitalize().replace('_', ' ')} "
                                f"must be int object. Not {type(value).__name__}.")
            if value not in [4, 8, 16, 64]:
                raise ValueError('Ram memory value must be in [4, 8, 16, 64].')

        elif var_name == 'built_in_memory':
            if not isinstance(value, int):
                raise TypeError(f"{var_name.capitalize().replace('_', ' ')} "
                                f"must be int object. Not {type(value).__name__}.")
            if value not in [128, 256, 512, 1024]:
                raise ValueError('Built in memory value must be in [128, 256, 512, 1024].')

        elif var_name == 'type_drive':
            if not isinstance(value, str):
                raise TypeError(f'Type of Hard Drive must be str object. Not {type(value).__name__}.')
            types = ['SSD', 'SSHD', 'HDD']
            if value.upper() not in types:
                raise ValueError(f'Wrong value entered. It should match one of -> {types}.')

    @property
    def ram_memory(self):
        return self._ram_memory

    @ram_memory.setter
    def ram_memory(self, value):
        Laptop._validate_value(self, value, 'ram_memory')
        self._ram_memory = value

    @property
    def built_in_memory(self):
        return self._built_in_memory

    @built_in_memory.setter
    def built_in_memory(self, value):
        Laptop._validate_value(self, value, 'built_in_memory')
        self._built_in_memory = value

    @property
    def type_drive(self):
        return self._type_drive

    @type_drive.setter
    def type_drive(self, value):
        Laptop._validate_value(self, value, 'type_drive')
        self._type_drive = value
