import unittest
from project.worker import Worker
from project.person import Person
from unittest.mock import patch

def setUpModule():
    print('setting up module...')
    global worker
    worker = Worker('Name', 'Surname')


class TestWorkerJobPosition(unittest.TestCase):

    @patch.object(Worker, '_get_job_position')
    def test_get_job_position(self, mocked_method):
        mocked_method.return_value = 'seller'
        actual = worker._get_job_position()
        expected = 'seller'
        self.assertEqual(actual, expected)

    def test_update_job_position(self):
        with self.assertRaises(AttributeError):
            worker.job_position = 'gamer'


class TestWorkerIdentity(unittest.TestCase):

    @patch.object(Person, '_get_identity')
    def test_worker_identity(self, mocked_method):
        mocked_method.return_value = 200000
        actual = Person._get_identity(worker)
        expected = 200000
        self.assertEqual(actual, expected)

    def test_update_identity(self):
        with self.assertRaises(AttributeError):
            worker.identity = 123456


class TestClassPersonAttributeWorkers(unittest.TestCase):

    def test_workers_attribute_after_create_an_instance(self):
        self.assertIn(worker, Person.workers)


if __name__ == '__main__':
    unittest.main(verbosity=2)