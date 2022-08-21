from project.person.person import Person
import time
import random
from project.database.database import *
from project.shop.shopping_cart import ShoppingCart


class Customer(Person):

    def __init__(self, shop_instance, name, surname, city, money):
        super().__init__(name, surname)
        self._email = f'{self.name}.{self.surname}{str(self.identity)[-3:]}@mail.com'
        self._city = city
        self._entry_time = time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())
        self._money = money
        self._shop = shop_instance
        self._shopping_cart = ShoppingCart()
        self._is_paid = False
        self._exit_time = None
        self._bill = None
        Person.customers.append(self)
        insert_data(self, database, 'customers')

    def __str__(self):
        return f'{super().__str__()}, ENTRY TIME: {self.entry_time}'

    @property
    def email(self):
        return self._email

    @property
    def city(self):
        return self._city

    @property
    def entry_time(self):
        return self._entry_time

    @property
    def shop(self):
        return self._shop

    @property
    def shopping_cart(self):
        return self._shopping_cart

    def make_action(self, count):
        for i in range(count):
            product = random.choice(self.shop.products)
            self.shopping_cart.items.append(product)
        self.pay_for_items()

    def pay_for_items(self):
        time.sleep(random.randint(1, 5))
        total = 0
        while self._is_paid is False:
            for product in self.shopping_cart.items:
                total += product.price_with_margin
            if self._money >= total:
                for product in self.shopping_cart.items:
                    self._shop._sold_products.append(product)
                    database.update_product('products', product.identity)
                    insert_data(product, database, 'sold')
                self._money -= total
                self._is_paid = True
                self._bill = total
                Customer.bye(self)
            else:
                self.shopping_cart.remove_product(self.shopping_cart.items[-1])
                total = 0

    def bye(self):
        self._exit_time = time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())
        print(f'{self}, LEFT AT TIME: {self._exit_time}')
        database.update_customer('customers', self)
