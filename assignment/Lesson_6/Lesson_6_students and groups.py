# solution 1
print('solution 1 ------------')
students = {
    'Ivanov': {'Python', 'SQL'},
    'Sidorov': {'JS', 'Front End'},
    'Petrov': {'Lavarel'},
    'Smirnov': {'Java', 'Python'},
    'Fedorov': {'Web design', 'Front End'},
    'Krivov': {'JS', 'Web design'}
}
for key, values in students.items():
    if len(values) > 1:
        print(f'{key} is in two or more groups')
    if 'Front End' not in values:
        print(f'{key} doesnt study front end')
    if 'Java' in values and 'Python' in values:
        print(f'{key} studies Python and Java')

# solution 2
print('')
print('solution 2 ------------')
groups = {
    'Java': ['Smirnov'],
    'Python': ['Ivanov', 'Smirnov'],
    'JS': ['Sidorov', 'Krivov'],
    'Web design': ['Fedorov', 'Krivov'],
    'SQL': ['Ivanov'],
    'Front End': ['Sidorov', 'Fedorov'],
    'Lavarel': ['Petrov']
}
iterable = [j for i in list(groups.values()) for j in i]
for item in set(iterable):
    if iterable.count(item) > 1:
        print(f'{item} is in 2 or more groups')
    if item not in groups.get('Front End'):
        print(f'{item} does not study Front End')
    if (item in groups.get('Python')) and (item in groups.get('Java')):
        print(f'{item} study both Python and Java')
