num = int(input('enter a number: '))
result = [x for x in range(1, int(num//2+1)) if not num % x]
result.append(num)
print(' '.join(list(map(str, result))))

