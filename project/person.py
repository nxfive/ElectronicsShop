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
            self._identity = Person._get_identity(self)
        else:
            self._identity = None

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
            return len(Person.customers) + 1
        elif self.__class__.__name__ == 'Worker':
            return random.randint(123456, 234567)

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

    @property
    def identity(self):
        return self._identity
