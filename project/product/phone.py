import random
from project.product.product import Product


class Phone(Product):

    def __init__(self, brand, prod_name, net_price):
        super().__init__(brand, prod_name, net_price)
        self._camera = Phone._choice_for_camera()
        self._is_keyboard = random.choice(('YES', 'NO'))
        if self._is_keyboard == 'NO':
            self._is_touch_screen = 'YES'
        else:
            self._is_touch_screen = random.choice(('YES', 'NO'))
        self._memory = Phone._add_memory()

    def __str__(self):
        return f'{super().__str__()}, net_price: {self.net_price}'

    @property
    def camera(self):
        return self.camera

    @property
    def is_keyboard(self):
        return self._is_keyboard

    @property
    def is_touch_screen(self):
        return self._is_touch_screen

    @property
    def memory(self):
        return self._memory

    @staticmethod
    def _add_memory():
        return random.choice([16, 32, 64, 128, 512])

    @staticmethod
    def _choice_for_camera():
        return random.choice([8, 10, 12, 14, 16, 18, 20])
