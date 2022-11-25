import datetime


class Employee:

    def __init__(self, name, day_salary):
        self.name = name
        self.day_salary = day_salary

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


u = Employee('Kate', 20)
u1 = Employee('Jane', 25)
print(f'comparing salary of employee {u.name} vs {u1.name}, {u.day_salary} > {u1.day_salary}? > {u > u1}')

a = Recruiter('alex', 10)
print(f'check salary for mentioned days {a.check_salary(10)}')
print(f'check salary for working days up to today excluding weekends {a.check_salary()}')

b = Developer('john', 20, ['java', 'python', 'c++'])
c = Developer('smith', 200, ['java', 'go', 'ruby'])
d = Developer('Kale', 500, ['assembler'])
print(a.work())
print(b.work())
print(c.work())

print(f'comparing tech stack of {b.name} and {c.name} equal? {b == c}')
print(f'comparing tech stack of {b.name} and {d.name} equal? {b == d}')

y = c + b
print(f'adding developers {c.name} and {b.name}, result> {y.name}, {y.tech_stack}')
