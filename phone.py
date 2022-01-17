from product import Product


class Phone(Product):

    def __init__(self, brand, name, net_price, is_camera=None, is_keyboard=None, is_touch_screen=None, memory=None):
        super().__init__(brand, name, net_price)
        self._is_camera = is_camera
        self._is_keyboard = is_keyboard
        self._is_touch_screen = is_touch_screen
        self._memory = memory

    @property
    def is_camera(self):
        return self._is_camera

    @is_camera.setter
    def is_camera(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'Value for camera must be bool object. Not {type(value).__name__}.')
        self._is_camera = value

    @property
    def is_keyboard(self):
        return self._is_keyboard

    @is_keyboard.setter
    def is_keyboard(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'Value for keyboard must be bool object. Not {type(value).__name__}.')
        self._is_keyboard = value

    @property
    def is_touch_screen(self):
        return self._is_touch_screen

    @is_touch_screen.setter
    def is_touch_screen(self, value):
        if not isinstance(value, bool):
            raise TypeError(f'Value for touch screen must be bool object. Not {type(value).__name__}.')
        self._is_touch_screen = value

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, value):
        if isinstance(value, int):
            if value in [16, 32, 64, 128, 512]:
                self._memory = value
            else:
                raise ValueError(f'Wrong value of memory. '
                                 f'Check if your input is [4, 8, 16, 32, 64].')
        else:
            raise TypeError(f'Value of memory must be int object. Not {type(value).__name__}.')

