import unittest
from project.person import Person
from parameterized import parameterized

test_params = [
    ('int_value', 12345),
    ('float_value', 12.5),
    ('int_value_in_single_quotes', '12345'),
    ('float_value_in_single_quotes', '12.5'),
    ('string_with_number_value_in_single_quotes', 'ABC12'),
    ('string_with_other_value_in_single_quotes', 'ABC#'),
]


class TestCreatePersonInstance(unittest.TestCase):

    @parameterized.expand(test_params)
    def test_name_validation(self, test_name, name):
        if not isinstance(name, str):
            self.assertRaises(TypeError, Person, name, 'Surname')
        else:
            self.assertRaises(ValueError, Person, name, 'Surname')

    @parameterized.expand(test_params)
    def test_surname_validation(self, test_name, surname):
        if not isinstance(surname, str):
            self.assertRaises(TypeError, Person, 'Name', surname)
        else:
            self.assertRaises(ValueError, Person, 'Name', surname)


class TestUpdatePersonInstance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class: {cls.__name__}.')
        cls.person = Person('Name', 'Surname')

    @parameterized.expand(test_params)
    def test_update_name(self, test_name, name):
        if not isinstance(name, str):
            with self.assertRaises(TypeError):
                self.person.name = name
        else:
            with self.assertRaises(ValueError):
                self.person.name = name

    @parameterized.expand(test_params)
    def test_update_surname(self, test_name, surname):
        if not isinstance(surname, str):
            with self.assertRaises(TypeError):
                self.person.surname = surname
        else:
            with self.assertRaises(ValueError):
                self.person.surname = surname


class TestClassAttributes(unittest.TestCase):
    """
    Test if class attributes as `customers` and `workers`
    are empty after create an instance from Person class.
    """
    @classmethod
    def setUpClass(cls):
        print(f'setting up class: {cls.__name__}')
        cls.person = Person('Name', 'Surname')

    def test_class_attribute_workers(self):
        self.assertEqual(Person.workers, [])

    def test_class_attribute_customers(self):
        self.assertEqual(Person.customers, [])


class TestIdentityValue(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class: {cls.__name__}')
        cls.person = Person('Name', 'Surname')

    def test_identity_should_be_None(self):
        self.assertIsNone(self.person.identity, 'identity is not None')


if __name__ == '__main__':
    unittest.main(verbosity=2)
