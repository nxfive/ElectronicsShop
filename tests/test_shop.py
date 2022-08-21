import unittest
from parameterized import parameterized
from project.shop.shop import Shop
from unittest.mock import patch
from project.product.phone import Phone
from project.product.laptop import Laptop
from project.utils.errors import NoSpaceError

test_params = [
    ('int_value', 12345),
    ('float_value', 12.5),
    ('int_value_in_single_quotes', '12345'),
    ('float_value_in_single_quotes', '12.5'),
    ('string_with_number_value_in_single_quotes', 'ABC12'),
    ('string_with_other_value_in_single_quotes', 'ABC#'),
]


class TestCreateShopInstance(unittest.TestCase):

    @parameterized.expand(test_params)
    def test_name_validation(self, test_name, name):
        """
            Name validation test >
        """
        if not isinstance(name, str):
            self.assertRaises(TypeError, Shop, name, 20, 20)
        else:
            self.assertRaises(ValueError, Shop, name, 20, 20)

    @parameterized.expand(test_params[1:])
    def test_max_capacity_validation(self, test_name, max_capacity):
        """
            Max capacity validation test >
        """
        if not isinstance(max_capacity, int):
            self.assertRaises(TypeError, Shop, 'Name', max_capacity, 20)
        else:
            self.assertRaises(ValueError, Shop, 'Name', max_capacity, 20)

    @parameterized.expand(test_params[1:])
    def test_amount_of_workers_validation(self, test_name, amount_of_workers):
        """
            Amount of workers value validation test >
        """
        if not isinstance(amount_of_workers, int):
            self.assertRaises(TypeError, Shop, 'Name', 20, amount_of_workers)
        else:
            self.assertRaises(ValueError, Shop, 'Name', 20, amount_of_workers)


class TestUpdateShopInstance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print(f'setting up class: {cls.__name__}')
        cls.shop = Shop('Name', 20, 20)

    @parameterized.expand(test_params)
    def test_name_update_validation(self, test_name, name):
        """
            Name update validation test >
        """
        if not isinstance(name, str):
            with self.assertRaises(TypeError):
                self.shop.name = name
        else:
            with self.assertRaises(ValueError):
                self.shop.name = name

    @parameterized.expand(test_params[1:])
    def test_max_capacity_update_validation(self, test_name, max_capacity):
        """
            Max capacity update validation test >
        """
        if not isinstance(max_capacity, int):
            with self.assertRaises(TypeError):
                self.shop.max_capacity = max_capacity
        else:
            with self.assertRaises(ValueError):
                self.shop.max_capacity = max_capacity

    @parameterized.expand(test_params[1:])
    def test_amount_of_workers_validation(self, test_name, amount_of_workers):
        """
            Amount of workers validation test >
        """
        if not isinstance(amount_of_workers, int):
            with self.assertRaises(TypeError):
                self.shop.amount_of_workers = amount_of_workers
        else:
            with self.assertRaises(ValueError):
                self.shop.amount_of_workers = amount_of_workers


class TestCreateWorkers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print(f'setting up class: {cls.__name__}')
        cls.shop = Shop('Name', 20, 20)

    @staticmethod
    def check_name_surname_pair(name, surname):
        """
            The function check if pairs of name and surname value
            are correctly related.
        """
        if name.endswith('a'):
            return True if not surname.endswith(('ski', 'cki', 'sny', 'zki', 'y')) else False
        elif not name.endswith('a'):
            return True if not surname.endswith(('ska', 'cka', 'zka', 'sna', 'a')) else False

    def test_amount_of_created_workers(self):
        """
            Test if amount of workers are the same
            as amount of created worker instance
        """
        workers = self.shop._create_workers()
        self.assertEqual(len(workers), self.shop.amount_of_workers)

    def test_correct_values_pair_for_worker(self):
        workers = self.shop._create_workers()
        for worker in workers:
            self.assertTrue(self.check_name_surname_pair(worker.name, worker.surname))


class TestCreateProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print()
        print(f'setting up class: {cls.__name__}')
        cls.shop = Shop('Name', 20, 20)

    @patch('random.choice')
    def test_create_laptop_instances(self, mocked_choice):
        mocked_choice.return_value = 'Laptop'
        self.shop.products.clear()
        for product in self.shop.products:
            self.assertIsInstance(product, Laptop)

    @patch('random.choice')
    def test_create_phone_instances(self, mocked_choice):
        mocked_choice.return_value = 'Phone'
        self.shop.products.clear()
        for product in self.shop.products:
            self.assertIsInstance(product, Phone)


class TestAddProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class: {cls.__name__}')
        cls.shop = Shop('Name', 20, 5)

    def test_add_new_product_phone_with_no_space(self):
        """
            Add new product with no space test >
            Shop instance should raise an error when
            adds another product.
        """
        self.assertRaises(NoSpaceError, self.shop.add_product, 2)

    def test_add_new_product_laptop_with_space(self):
        """
            Add new product test >
            Capacity of shop instance must increase by 1 to add
            a new product.
        """
        first = len(self.shop.products)
        self.shop.max_capacity += 1
        self.shop.add_product(1)
        second = len(self.shop.products)
        self.assertEqual(first + 1, second)


if __name__ == '__main__':
    unittest.main(verbosity=2)
