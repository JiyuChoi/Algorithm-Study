n = int(input())
students = sorted([input().split() for _ in range(n)], key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])