people_training = int(input())

training = 0
not_training = 0
back_training = 0
chest_training = 0
legs_training = 0
abs_training = 0
protein_shake = 0
protein_bar = 0

for people in range(people_training):
    fitness_work_out = input()

    if fitness_work_out == "Back":
        back_training += 1
        training += 1
    elif fitness_work_out == "Chest":
        chest_training += 1
        training += 1
    elif fitness_work_out == "Legs":
        legs_training += 1
        training += 1
    elif fitness_work_out == "Abs":
        abs_training += 1
        training += 1
    elif fitness_work_out == "Protein shake":
        protein_shake += 1
        not_training += 1
    elif fitness_work_out == "Protein bar":
        protein_bar += 1
        not_training += 1

print(f"{back_training} - back")
print(f"{chest_training} - chest")
print(f"{legs_training} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{training/people_training*100:.2f}% - work out")
print(f"{not_training/people_training*100:.2f}% - protein")