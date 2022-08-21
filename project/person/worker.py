import random
from project.person.person import Person
from project.database.database import *


class Worker(Person):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._job_position = random.choice(['seller', 'cashier'])
        Worker.workers.append(self)
        insert_data(self, database, 'workers')

    @property
    def job_position(self):
        return self._job_position
