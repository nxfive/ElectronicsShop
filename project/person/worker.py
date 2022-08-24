import random
from project.person.person import Person
from project.database.database import *


class Worker(Person):

    def __init__(self, shop_instance, name, surname):
        super().__init__(name, surname)
        self._job_position = random.choice(['seller', 'cashier'])
        self._shop = shop_instance
        Worker.workers.append(self)
        insert_data(self, self.shop.database, 'workers')

    @property
    def job_position(self):
        return self._job_position

    @property
    def shop(self):
        return self._shop
