def size_transformation(size, country):
    countries = {
        'россия': 42,
        'германия': 36,
        'сша': 8,
        'франция': 38,
        'великобритания': 24}
    sizes = ['xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl']
    if (country in countries.keys()) and (size in sizes):
        return f'your size is {countries.get(country) + 2 * sizes.index(size)}'
    elif size not in sizes:
        return f"there is no such size {size}, should be in {sizes}"
    elif country not in countries.keys():
        return f'there is no such country {country}, should be in {countries.keys()}'


size, country = input('enter size, country (separate by space): ').strip().lower().split(' ')
print(size_transformation(size, country))

