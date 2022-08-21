import unittest
from project.shop.shop import Shop
from project.product.laptop import Laptop
from project.person.customer import Customer


class TestCustomerPurchase(unittest.TestCase):

    def setUp(self):
        print(f'setting up class: {self.__class__.__name__}')
        self.shop = Shop('Shop', 5, 20)
        self.product = Laptop('Brand', 'Name', 2000)
        self.customer = Customer(self.shop, 'Nikola', 'Jones', 'Miami', 2600)
        self.shop.products.append(self.product)
        self.customer.shopping_cart.items.append(self.product)
        self.customer.make_action(0)

    def test_customer_bill_for_product(self):
        """
            Test customer bill >
            if amount on bill is the same as
            amount for product.
        """
        self.assertEqual(self.customer._bill, 2000*1.25)

    def test_customer_pay_for_product(self):
        """
            Test customer payment >
            If customer has enough money
            should pay for product.
            is_paid = True.
        """
        self.assertTrue(self.customer._is_paid)
