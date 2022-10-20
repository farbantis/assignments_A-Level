import random


def fizz_buzz(fizz, buzz, x, my_file):
    """calculates fizz buzz sequence, prints it out and saves to a file"""
    arr = []
    for digit in range(1, x + 1):
        if not digit % fizz and not digit % buzz:
            arr.append('FB')
        elif not digit % fizz:
            arr.append('F')
        elif not digit % buzz:
            arr.append('B')
        else:
            arr.append(str(digit))
    print(f"{fizz}, {buzz}, {x} => {' '.join(arr)}")
    with open(my_file, 'a+') as f:
        print(f"{' '.join(arr)}", file=f)

# open file to populate with random fizz-buzz numbers, totally 20 sets
with open('Lesson_2_fizz_buzz data from file.txt', 'w') as file:
    for _ in range(20):
        print(f"{str(random.randint(1, 10))} {str(random.randint(1, 10))} {str(random.randint(15, 20))}", file=file)

    # now read newly created data
with open('Lesson_3_fizz_buzz data from file.txt', 'r+') as file:
    file.seek(0)
    # ask for a file name where to save those 20 fizz-buzz sets
    desired_file_name = input('enter the file name to save fizz buzz, can skip by pressing <enter>: ')
    if not desired_file_name:
        my_file = 'fizz_buzz.txt'
    else:
        my_file = f"{desired_file_name.split('.')[0]}.txt"
    for line in file:
        # read each row of a file and call a function to calculate fizz buzz
        f, b, x = list(map(int, line.replace("/n", "").split()))
        fizz_buzz(f, b, x, my_file)

