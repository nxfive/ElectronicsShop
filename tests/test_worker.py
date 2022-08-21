import unittest
from project.person.worker import Worker


class TestClassPersonAttributeWorkers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f'setting up class: {cls.__name__}')
        cls.worker = Worker('Name', 'Surname')

    def test_attribute_workers_after_create_an_instance(self):
        self.assertIn(self.worker, Worker.workers)


if __name__ == '__main__':
    unittest.main(verbosity=2)
