from project.person.person import Person
from project.utils.errors import ChangeContainerSizeError
import random
from project.database.database import *


class Worker(Person):
    # how many employees we can hire in total
    _number_of_jobs = 5

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._job_position = random.choice(['seller', 'cashier'])
        Person.workers.append(self)
        insert_data(self, database, 'workers')

    @property
    def job_position(self):
        return self._job_position

    @property
    def number_of_jobs(self):
        return Worker._number_of_jobs

    @number_of_jobs.setter
    def number_of_jobs(self, value):
        if isinstance(value, int) and value >= len(Person.workers):
            Worker._number_of_jobs = value
        else:
            raise ChangeContainerSizeError(value, f'Cannot change the jobs to {value} place/s.')
