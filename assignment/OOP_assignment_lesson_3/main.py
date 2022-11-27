from app import Employee, EmailAlreadyExistsException
from datetime import datetime
import traceback


def main(person):
    try:
        exec(person)
    except EmailAlreadyExistsException as em:
        print(f'{em.args[1]}, {em.args[0]}')
        with open('log.txt', 'a') as f:
            print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} | {traceback.format_exc()}', file=f)


if __name__ == '__main__':
    mylist = ["staff_1 = Employee('Smith', 25, 'smith@gmail.com')",
              "staff_2 = Employee('John', 35, 'john@gmail.com')",
              "staff_3 = Employee('Kale', 45, 'smith@gmail.com')",
              "staff_4 = Employee('Fitch', 55, 'fitch@gmail.com')"
              ]
    for person in mylist:
        main(person)




