fizz, buzz, x = map(int, input("enter 3 numbers separated by ',': ").strip().split(','))
for digit in range(1, x+1):
    if not digit % fizz and not digit % buzz:
        print('FB', end=" ")
    elif not digit % fizz:
        print('F', end=" ")
    elif not digit % buzz:
        print('B', end=" ")
    else:
        print(digit, end=" ")
