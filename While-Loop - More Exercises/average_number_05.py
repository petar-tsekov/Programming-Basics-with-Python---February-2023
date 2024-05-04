
iteration_number = int(input())

total_number = 0

for number in range(iteration_number):
    numbers_entered = int(input())
    total_number += numbers_entered

print(f"{total_number / iteration_number:.2f}")
