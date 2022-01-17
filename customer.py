from person import Person
import time


class Customer(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.entry_time = Customer.get_entry_time()
        self.money = Customer._add_your_money()
        self.shopping_cart = []
        self.is_paid = False
        self.exit_time = None

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
        for idx, product in enumerate(self.shopping_cart):
            if product_name == product[2]:
                self.shopping_cart.remove(self.shopping_cart[idx])

    def list_shopping_cart(self):
        for product in self.shopping_cart:
            print(f'{product.__class__.__name__}, Brand: {product[0]}\nName: {product[1]}\nPrice: {product[2]}.')

    def add_customer_to_list(self):
        Person.customers.append({'name': f'{self.name}', 'surname': f'{self.surname}',
                                 'identity': f'{self.identity}'.zfill(3)})

    def paid_for_items(self):
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
        else:
            print('You do not have enough money for these purchases.')

    @staticmethod
    def display_list_of_customers():
        for customer in Person.customers:
            for key, value in customer.items():
                print(f'{key}: {value}')
            print(20 * '-')

    @staticmethod
    def hello():
        print('Good morning')

    def bye(self):
        print('Goodbye')
        self.exit_time = time.strftime('%H:%M:%S', time.localtime())
