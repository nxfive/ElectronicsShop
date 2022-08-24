import random
from project.product.product import Product


class Laptop(Product):

    def __init__(self, shop_instance, brand, prod_name, net_price):
        super().__init__(shop_instance, brand, prod_name, net_price)
        self._ram_memory = random.choice([4, 8, 16, 64])
        self._built_in_memory = random.choice([128, 256, 512, 1024])
        self._type_drive = random.choice(['SSD', 'SSHD', 'HDD'])

    def __str__(self):
        return f'{super().__str__()}, net_price: {self.net_price}'

    @property
    def ram_memory(self):
        return self._ram_memory

    @property
    def built_in_memory(self):
        return self._built_in_memory

    @property
    def type_drive(self):
        return self._type_drive
