students_count = int(input())

top_stundets = 0
b_students = 0
c_students = 0
f_students = 0
total_students = 0
total_grade = 0

for students in range(students_count):
    student_grade = float(input())
    total_students += 1
    total_grade += student_grade

    if 2 <= student_grade <= 2.99:
        f_students += 1
    elif 3 <= student_grade <= 3.99:
        c_students += 1
    elif 4 <= student_grade <= 4.99:
        b_students += 1
    else:
        top_stundets += 1

print(f"Top students: {top_stundets/total_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {b_students/total_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {c_students/total_students * 100:.2f}%")
print(f"Fail: {f_students/total_students * 100:.2f}%")
print(f"Average: {total_grade/total_students:.2f}")