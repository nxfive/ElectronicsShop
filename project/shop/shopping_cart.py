from prettytable import PrettyTable


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def update_product(self, product, action, n=1):
        """
            Function updates product with action:
            - `add` - add one another the same product
            - `del` - remove one product
            - `n` - how many times
        """
        if action == 'add' and n == 1:
            self.items.append(product)
        elif action == 'add' and n > 1:
            for i in range(n):
                self.items.append(product)
        else:
            raise ValueError('Value of `n` must be positive.')
        if action == 'remove':
            self.items.remove(product)

    def remove_product(self, product):
        self.items.remove(product)

    def list_shopping_cart(self):
        shopping_cart_table = PrettyTable()
        shopping_cart_table.title = 'SHOPPING CART'
        shopping_cart_table.field_names = ['No.', 'Category', 'Brand', 'Name', 'Price']
        for index, product in enumerate(self.items):
            shopping_cart_table.add_row([index+1, product[0], product[1], product[2], product[3]])
        print(shopping_cart_table)
