
number_one = int(input())
number_two = int(input())
command_entered = input()

result = 0
even_odd_number = ""

if command_entered == "+" or command_entered == "-" or command_entered == "*":
    if command_entered == "+":
        result = number_one + number_two
    elif command_entered == "-":
        result = number_one - number_two
    elif command_entered == "*":
        result = number_one * number_two
    if result % 2 == 0:
        even_odd_number = "even"
    else:
        even_odd_number = "odd"

    print(f"{number_one} {command_entered} {number_two} = {result} - {even_odd_number}")

elif command_entered == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")

elif command_entered == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")

