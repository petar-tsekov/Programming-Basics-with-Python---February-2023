
unsatisfactory_grades = int(input())

total_score = 0
task_qty = 0
task_failed = 0
last_problem = ""
avarege_points = 0

while True:

    task_name = input()

    if task_name == "Enough":
        break
    task_grade = int(input())

    if task_grade <= 4:
        task_failed += 1

        if task_failed == unsatisfactory_grades:
            print(f"You need a break, {task_failed} poor grades.")
            break
    task_qty += 1
    total_score += task_grade
    last_problem = task_name

if task_failed != unsatisfactory_grades:
    avarege_points = total_score / task_qty
    print(f"Average score: {avarege_points:.2f}")
    print(f"Number of problems: {task_qty}")
    print(f"Last problem: {last_problem}")

