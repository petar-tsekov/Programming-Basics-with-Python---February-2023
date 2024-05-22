num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    first_digit = i % 10
    second_digit = i // 10 % 10
    third_digit = i // 100 % 10
    fourth_digit = i // 1000 % 10
    fifth_digit = i // 10000 % 10
    sixth_digit = i // 100000 % 10

    even_sum = first_digit + third_digit + fifth_digit
    odd_sum = second_digit + fourth_digit + sixth_digit

    if even_sum == odd_sum:
        print(i, end=" ")