command_entered = input()
prime_number_sum = 0
not_prime_number_sum = 0

while command_entered != "stop":
    command_entered_int = int(command_entered)

    if command_entered_int < 0:
        print(f"Number is negative.")
        command_entered = input()
        continue
    count = 0
    for number in range(1, command_entered_int + 1):

        if command_entered_int % number == 0:
            count += 1
    if count == 2:
        prime_number_sum += command_entered_int
    else:
        not_prime_number_sum += command_entered_int
    command_entered = input()

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {not_prime_number_sum}")




