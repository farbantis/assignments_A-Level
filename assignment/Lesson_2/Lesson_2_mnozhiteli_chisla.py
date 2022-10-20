num = input('enter number greater 0: ')
for index, digit in enumerate(num[::-1]):
    print(f'{digit} * 10**{index} = {int(digit) * 10**int(index)}')

#  второй вариант
i = 0
num1 = int(input('enter number greater 0: '))
while num1 > 0:
    print(f'{num1 % 10} * 10**{i} = {num1 % 10 * 10**i}')
    i += 1
    num1 //= 10
