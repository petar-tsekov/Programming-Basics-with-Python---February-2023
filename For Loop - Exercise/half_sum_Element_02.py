import sys

max_num = -sys.maxsize
total_sum = 0

iterations_entered = int(input())

for x in range(iterations_entered):
    number_entered = int(input())

    if number_entered > max_num:
        max_num = number_entered

    total_sum += number_entered

if max_num == total_sum - max_num:
    print("Yes")
    print(f"Sum = {total_sum}")
else:
    print("No")
    total_sum = total_sum - max_num
    print(f"Diff = {abs(max_num - total_sum)}")
