num_of_students = int(input())

students = {}

for _ in range(num_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    grades_as_str = ' '.join([str(f'{grade:.2f}') for grade in value])
    avg_grade = sum(value) / len(value)
    print(f"{key} -> {grades_as_str} (avg: {avg_grade:.2f})")
