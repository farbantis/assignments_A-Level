import datetime
from pathlib import Path


class EmailAlreadyExistsException(Exception):
    def __init__(self, text, email):
        self.text = text
        self.email = email


class Employee:
    FILE_NAME = 'emails.txt'

    def __init__(self, name, day_salary, email):
        self.name = name
        self.day_salary = day_salary
        if self.save_email(email):
            self.email = email

    def save_email(self, email):
        if self.validate(email):
            with open('emails.txt', 'a+') as f:
                print(email, file=f)
            return True

    @classmethod
    def validate(cls, email):
        mode_ch = 'r' if Path(cls.FILE_NAME).exists() else 'a+'
        with open(cls.FILE_NAME, mode_ch) as f:
            if email in f.read():
                raise EmailAlreadyExistsException('this email already exists', email)
            return True

    def check_salary(self, days=0):
        if not days:
            today = datetime.date.today()
            for i in range(1, today.day):
                if datetime.date(today.year, today.month, i).isoweekday() not in [6, 7]:
                    days += 1
        return self.day_salary * days

    def work(self):
        return 'I come to the office.'

    def __eq__(self, other):
        return self.day_salary == other.day_salary

    def __gt__(self, other):
        return self.day_salary > other.day_salary

    def __ge__(self, other):
        return self.day_salary >= other.day_salary

    def __lt__(self, other):
        return self.day_salary < other.day_salary

    def __le__(self, other):
        return self.day_salary <= other.day_salary

    def __ne__(self, other):
        return self.day_salary != other.day_salary

    def __str__(self):
        return f'position is: {self.name}'


class Recruiter(Employee):
    def work(self):
        initial_str = super(Recruiter, self).work()
        return initial_str[:-1] + ' and start coding'


class Developer(Employee):
    def __init__(self, name: str, day_salary: int, tech_stack: list[str, ...] = None):
        super(Developer, self).__init__(name, day_salary)
        if not tech_stack:
            tech_stack = []
        self.tech_stack = tech_stack

    def __add__(self, other):
        self.tech_stack.extend(other.tech_stack)
        return Developer(name=f'{self.name} {other.name}', day_salary=0, tech_stack=list(set(self.tech_stack)))

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __str__(self):
        return f'position is: {self.name}'

    def work(self):
        initial_str = super(Developer, self).work()
        return initial_str[:-1] + ' and start hiring'

