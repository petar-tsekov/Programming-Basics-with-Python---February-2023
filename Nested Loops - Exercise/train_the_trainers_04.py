judges_count = int(input())
presentation_name = input()

total_grade = 0
count_grades = 0
total_count_grades = 0
while presentation_name != "Finish":

    total_grade_presentation = 0
    count_grades_presentation = 0


    for grade in range(judges_count):
        grade_entered = float(input())
        count_grades_presentation += 1
        total_grade_presentation += grade_entered
    total_grade += total_grade_presentation

    total_count_grades += count_grades_presentation

    print(f"{presentation_name} - {total_grade_presentation / judges_count:.2f}.")

    presentation_name = input()

print(f"Student's final assessment is {total_grade /total_count_grades:.2f}.")


