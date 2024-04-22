
iterations_entered = int(input())

number_one = 0
number_two = 0
number_tree = 0
number_four = 0
number_five = 0

for x in range(iterations_entered):
    number_entered = int(input())

    if number_entered < 200:
        number_one += 1
    elif 200 <= number_entered <= 399:
        number_two += 1
    elif 400 <= number_entered <= 599:
        number_tree += 1
    elif 600 <= number_entered <= 799:
        number_four += 1
    elif number_entered >= 800:
        number_five += 1

p1 = number_one / iterations_entered * 100
p2 = number_two / iterations_entered * 100
p3 = number_tree / iterations_entered * 100
p4 = number_four / iterations_entered * 100
p5 = number_five / iterations_entered * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")



