import random
from project.utils import input_validation as validate


class Person:
    customers = []
    workers = []

    def __init__(self, name, surname):
        validate(name, 'name')
        self._name = name
        validate(surname, 'surname')
        self._surname = surname
        if self.__class__.__name__ == 'Customer' or self.__class__.__name__ == 'Worker':
            self.identity = Person._get_identity(self)
        else:
            self.identity = None

    def __str__(self):
        if not self.identity:
            return f"{self.__class__.__name__}\nName: {self.name}\nSurname: {self.surname}\n--------------------"
        return f"{self.__class__.__name__}\nName: {self.name}\n" \
               f"Surname: {self.surname}\nID: {self.identity}\n--------------------"

    def __repr__(self):
        if not self.identity:
            return f"{self.__class__.__name__}=(name: {self.name}, surname: {self.surname})"
        return f"{self.__class__.__name__}=(name: {self.name}, surname: {self.surname}, identity: {self.identity})"

    def _get_identity(self):
        if self.__class__.__name__ == "Customer":
            self.identity = len(Person.customers) + 1
        elif self.__class__.__name__ == 'Worker':
            self.identity = random.randint(123456, 234567)
        return self.identity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        validate(value, 'name')
        self._name = value

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        validate(value, 'surname')
        self._surname = value
