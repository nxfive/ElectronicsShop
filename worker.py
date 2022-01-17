from person import Person
import random


class Worker(Person):
    # how many employees we can hire in total
    _number_of_jobs = 5

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._job_position = Worker._get_job_position()

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

    def add_worker_to_list(self):
        Person.workers.append({'identity': f'{self.identity}', 'name': f'{self.name}',
                               'surname': f'{self.surname}', 'job position': f'{self.job_position}'})

    @staticmethod
    def display_list_of_workers():
        for worker in Person.workers:
            for key, val in worker.items():
                print(f'{key}: {val}')
            print(20 * '-')
