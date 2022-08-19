from project.person.person import Person
import time
import random
from project.database.database import *
from project.shop.shopping_cart import ShoppingCart


class Customer(Person):

    def __init__(self, shop_instance, name, surname, city, money):
        super().__init__(name, surname)
        self.email = f'{self.name}.{self.surname}{str(self.identity)[-3:]}@mail.com'
        self.city = city
        self.entry_time = Customer.get_entry_time()
        self.money = money
        self.shop = shop_instance
        self.shopping_cart = ShoppingCart()
        self.is_paid = False
        self.exit_time = None
        self.bill = None
        Person.customers.append(self)
        insert_data(self, database, 'customers')

    def __str__(self):
        return f'{super().__str__()}, ENTRY TIME: {self.entry_time}'

    @staticmethod
    def get_entry_time():
        return time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())

    def make_action(self, count):
        for i in range(count):
            product = random.choice(self.shop.products)
            self.shopping_cart.items.append(product)
        self.pay_for_items()

    def pay_for_items(self):
        time.sleep(random.randint(1, 5))
        total = 0
        while self.is_paid is False:
            for product in self.shopping_cart.items:
                total += product.price_with_margin
            if self.money >= total:
                for product in self.shopping_cart.items:
                    database.update_product('products', product.identity)
                    insert_data(product, database, 'sold')
                self.money -= total
                self.is_paid = True
                self.bill = total
                Customer.bye(self)
            else:
                self.shopping_cart.remove_product(self.shopping_cart.items[-1])
                total = 0

    def bye(self):
        self.exit_time = time.strftime('%H:%M:%S %d.%m.%Y', time.localtime())
        print(f'{self}, LEFT AT TIME: {self.exit_time}')
        database.update_customer('customers', self)

