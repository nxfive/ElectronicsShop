from project.person import Person
import random
from project import database
from prettytable import PrettyTable


class Worker(Person):
    # how many employees we can hire in total
    _number_of_jobs = 5

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._job_position = Worker._get_job_position()
        Person.workers.append(self)
        database.insert_data(self, database.db, 'Workers')

    @property
    def job_position(self):
        return self._job_position

    @staticmethod
    def _get_job_position():
        jobs = ['seller', 'cashier']
        return random.choice(jobs)

    @property
    def number_of_jobs(self):
        return Worker._number_of_jobs

    @number_of_jobs.setter
    def number_of_jobs(self, value):
        if isinstance(value, int) and value >= len(Person.workers):
            Worker._number_of_jobs = value
        else:
            print('We cannot hire a new employee.')

    @staticmethod
    def display_list_of_workers():
        workers_table = PrettyTable()
        workers_table.title = "LIST OF WORKERS"
        workers_table.field_names = ['No.', 'Name', 'Surname', 'Position', 'Identity']
        for index, worker in enumerate(Person.workers):
            workers_table.add_row([index+1, worker.name, worker.surname, worker.job_position, worker.identity])
        print(workers_table)

