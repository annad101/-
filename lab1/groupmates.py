
groupmates = [
    {
        "name": "Василий",
        "group": "bst2252",
        "age": 25,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Анна",
        "group": "bst2254",
        "age": 24,
        "marks": [5, 5, 3, 4, 4]
    },
    {
        "name": "Георгий",
        "group": "bst2252",
        "age": 22,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Валентина",
        "group": "bst2254",
        "age": 25,
        "marks": [5, 5, 5, 4, 5]
    },
    {
        "name": "Афанасий",
        "group": "bst2251",
        "age": 24,
        "marks": [4, 4, 3, 4, 5]
    }
]


def print_students(students):
    print("Имя студента".ljust(15),
          "Группа".ljust(10),
          "Возраст".ljust(10),
          "Оценки")

    for student in students:
        print(
            student["name"].ljust(15),
            student["group"].ljust(10),
            str(student["age"]).ljust(10),
            str(student["marks"])
        )

    print()


def filter_students(students, avg_mark):
    result = []

    for student in students:
        average = sum(student["marks"]) / len(student["marks"])

        if average > avg_mark:
            result.append(student)

    return result


print("Все студенты:\n")
print_students(groupmates)

print("Студенты со средним баллом выше 4:\n")
filtered = filter_students(groupmates, 4)
print_students(filtered)
