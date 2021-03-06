import random
from product import Product


class Laptop(Product):

    def __init__(self, brand, name, net_price):
        super().__init__(brand, name, net_price)
        self._ram_memory = Laptop._add_ram_memory()
        self._built_in_memory = Laptop._add_built_in_memory()
        self._type_drive = Laptop._add_type_drive()

    def __str__(self):
        return f'{super().__str__()}, Price: {self.price_with_margin}\nRAM memory: {self.ram_memory}\n' \
               f'Built-in memory: {self.built_in_memory}\nType of drive: {self.type_drive}'

    @property
    def ram_memory(self):
        return self._ram_memory

    @property
    def built_in_memory(self):
        return self._built_in_memory

    @property
    def type_drive(self):
        return self._type_drive

    @staticmethod
    def _add_ram_memory():
        return random.choice([4, 8, 16, 64])

    @staticmethod
    def _add_built_in_memory():
        return random.choice([128, 256, 512, 1024])

    @staticmethod
    def _add_type_drive():
        return random.choice(['SSD', 'SSHD', 'HDD'])
