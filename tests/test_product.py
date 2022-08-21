import unittest
from project.product.product import Product
from parameterized import parameterized


test_params = [
    ('int_value', 12345),
    ('float_value', 12.5),
    ('float_value_in_single_quotes', '12.5'),
    ('string_with_other_value_in_single_quotes', 'ABC#'),
    ('int_value_in_single_quotes', '12345'),
    ('string_with_number_value_in_single_quotes', 'ABC12'),
]


class TestCreateProductInstance(unittest.TestCase):

    @parameterized.expand(test_params)
    def test_brand_validation(self, test_name, brand):
        """
            Brand input validation test >
        """
        if not isinstance(brand, str):
            self.assertRaises(TypeError, Product, brand, 'Name')
        else:
            self.assertRaises(ValueError, Product, brand, 'Name')

    @parameterized.expand(test_params[:4])
    def test_name_validation(self, test_name, prod_name):
        """
            Name input validation test >

            test_params[:4], because last two (index 4, index 5) of
            test_params list shouldn't pass this tests.
        """
        if not isinstance(prod_name, str):
            self.assertRaises(TypeError, Product, 'Brand', prod_name)
        else:
            self.assertRaises(ValueError, Product, 'Brand', prod_name)


class TestUpdateProductInstance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print(f'setting up class: {cls.__name__}')
        cls.product = Product('Brand', 'Name')

    @parameterized.expand(test_params)
    def test_brand_update(self, test_name, brand):
        """
            Brand update validation test >
        """
        if not isinstance(brand, str):
            with self.assertRaises(TypeError):
                self.product.brand = brand
        else:
            with self.assertRaises(ValueError):
                self.product.brand = brand

    @parameterized.expand(test_params[:4])
    def test_name_update(self, test_name, prod_name):
        """
            Name update validation test >

            test_params[:4], because last two (index 4, index 5) of
            test_params list shouldn't pass this tests.
        """
        if not isinstance(prod_name, str):
            with self.assertRaises(TypeError):
                self.product.prod_name = prod_name
        else:
            with self.assertRaises(ValueError):
                self.product.prod_name = prod_name


class TestAllPriceAttributes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print(f'setting up class: {cls.__name__}')
        cls.product = Product('Name', 'Surname')

    @parameterized.expand([
        ('string of numbers', '2000'),
        ('string with no alpha-numeric char', '2##0'),
        ('negative integer', -1),
        ('negative float', -0.1),
    ])
    def test_set_net_price(self, test_name, price):
        """
            Price set validation test >
        """
        if isinstance(price, str):
            with self.assertRaises(TypeError):
                self.product.net_price = price
        else:
            with self.assertRaises(ValueError):
                self.product.net_price = price

    def test_convert_price_with_margin(self):
        """
            Test convert price with margin >
        """
        self.product.net_price = 2000
        self.assertEqual(self.product.price_with_margin, 2500)

    def test_convert_price_with_margin_to_eur(self):
        """
            Test convert price with margin to eur >
        """
        self.product.net_price = 2000
        self.assertEqual(self.product._price_with_margin_eur, 625)

    def test_convert_price_with_margin_to_usd(self):
        """
            Test convert price with margin to usd >
        """
        self.product.net_price = 2000
        self.assertAlmostEqual(self.product._price_with_margin_usd, 543.48)

    def test_deleting_all_prices(self):
        """
            Delete all prices test >
            If net_price delete, other prices
            should change to None.
        """
        self.product.net_price = 2000
        self.assertIsNotNone(self.product.price_with_margin)
        self.assertIsNotNone(self.product._price_with_margin_eur)
        self.assertIsNotNone(self.product._price_with_margin_usd)
        del self.product.net_price
        self.assertIsNone(self.product.price_with_margin)
        self.assertIsNone(self.product._price_with_margin_eur)
        self.assertIsNone(self.product._price_with_margin_usd)


if __name__ == '__main__':
    unittest.main()
