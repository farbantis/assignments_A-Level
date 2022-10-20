from functools import reduce

my_list = list(map(int, input("enter numbers separated by ',': ").strip().split(',')))
print(sum(my_list))

# tough way..
my_list1 = reduce(lambda x, y: x+y,  my_list)
print(my_list1)
