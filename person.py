import random


class Person:
    customers = []
    workers = []

    def __init__(self, name, surname):
        Person._validation_input(name, 'name')
        self._name = name
        Person._validation_input(surname, 'surname')
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
        Person._validation_value(self, value, 'name')

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        Person._validation_value(self, value, 'surname')

    @staticmethod
    def _validation_input(value, var_name: str):
        """Validation before create an instance"""
        if not isinstance(value, str):
            raise TypeError(f'{var_name.capitalize()} cannot be {type(value).__name__} type.')
        if not value.isalpha():
            raise ValueError(f'{var_name.capitalize()} cannot include integers.')

    def _validation_value(self, value, var_name: str):
        """Validation of the value changed after instance was created."""
        if not isinstance(value, str):
            raise TypeError(f'{value.capitalize()} cannot be {type(value).__name__} type.')
        if not value.isalpha():
            raise ValueError(f'{value.capitalize()} cannot include integers.')

        if var_name == 'name':
            self._name = value
        else:
            self._surname = value

