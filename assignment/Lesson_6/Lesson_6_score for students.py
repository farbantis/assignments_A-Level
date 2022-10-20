students = {
    'Ivanov': 5,
    'Sidorov': 5,
    'Petrov': 10,
    'Smirnov': 8,
    'Fedorov': 6,
}
best_students_score = max(students.values())
worst_students_score = min(students.values())
average_score = sum(students.values()) / len(students)
for key, value in students.items():
    if value == worst_students_score:
        print(f'{key} is the worst student with score {value}, while average score is {average_score}')
    elif value == best_students_score:
        print(f'{key} is the best student with score {value}, while average score is {average_score}')


