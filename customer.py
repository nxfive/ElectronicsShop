from person import Person
from prettytable import PrettyTable
import time
import database


class Customer(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.entry_time = Customer.get_entry_time()
        self.money = Customer._add_your_money()
        self.shopping_cart = []
        self.is_paid = False
        self.exit_time = None
        Person.customers.append(self)

    def __str__(self):
        return f'Entry time: {self.entry_time}\n{super().__str__()}'

    @staticmethod
    def get_entry_time():
        return time.strftime('%H:%M:%S', time.localtime())

    @staticmethod
    def _add_your_money():
        while True:
            try:
                money = float(input("Enter how much money you've got: "))
                if money > 0:
                    return money
                else:
                    print('Value for money must be positive.')
            except ValueError:
                print('Value for money must be int or float object. Not str.')

    def add_to_shopping_cart(self, product_name, shop):
        for product in shop.products:
            if product.name == product_name:
                self.shopping_cart.append((product.__class__.__name__, product.brand,
                                           product.name, product.price_with_margin))

    def del_from_shopping_cart(self, product_name):
        for index, product in enumerate(self.shopping_cart):
            if product_name == product[2]:
                self.shopping_cart.remove(self.shopping_cart[index])

    def list_shopping_cart(self):
        shopping_cart_table = PrettyTable()
        shopping_cart_table.title = 'SHOPPING CART'
        shopping_cart_table.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
        for index, product in enumerate(self.shopping_cart):
            shopping_cart_table.add_row([index+1, product[0], product[1], product[2], product[3]])
        print(shopping_cart_table)

    def pay_for_items(self):
        total = 0
        for product in self.shopping_cart:
            # for product is tuple with items(class_name, brand, name, price)
            # so price is on index = 3
            total += product[3]
        print(f'Total price for items: {total}')
        if self.money >= total:
            self.money -= total
            self.is_paid = True
            print(f'The remaining amount: {self.money}')
            Customer.bye(self)
        else:
            print('You do not have enough money for these purchases.')

    @staticmethod
    def display_list_of_customers():
        customers_table = PrettyTable()
        customers_table.title = 'LIST OF CUSTOMERS'
        customers_table.field_names = ['No.', 'Name', 'Surname', 'Items']
        for index, customer in enumerate(Person.customers):
            customers_table.add_row([index+1, customer.name, customer.surname, customer.shopping_cart])
        print(customers_table)

    @staticmethod
    def hello():
        print('Good morning')

    def bye(self):
        print('Goodbye')
        self.exit_time = time.strftime('%H:%M:%S', time.localtime())
        database.insert_data(self, database.db, 'Customers')
