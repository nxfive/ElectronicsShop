import random
from product import Product


class Phone(Product):

    def __init__(self, brand, name, net_price):
        super().__init__(brand, name, net_price)
        self._is_camera = Phone._choice_for_camera()
        self._is_keyboard = Phone._choice_option()
        if self._is_keyboard == 'NO':
            self._is_touch_screen = 'YES'
        else:
            self._is_touch_screen = Phone._choice_option()
        self._memory = Phone._add_memory()

    def __str__(self):
        return f'{super().__str__()}\nCamera: {self.is_camera}\nKeyboard: {self.is_keyboard}' \
               f'\nTouch screen: {self.is_touch_screen}\nMemory: {self.memory}'

    @property
    def is_camera(self):
        return self._is_camera

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
    def _choice_option():
        return random.choice(['YES', 'NO'])

    @staticmethod
    def _add_memory():
        return random.choice([16, 32, 64, 128, 512])

    @staticmethod
    def _choice_for_camera():
        return random.choice([8, 10, 12, 14, 16, 18, 20])
