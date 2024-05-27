number_entered = int(input())
start_num = 1111
end_num = 9999

for numbers in range(start_num, end_num + 1):

    number_str = str(numbers)
    counter = 0
    for number in number_str:
        number_int = int(number)
        if number_int == 0:
            continue
        if number_entered % number_int == 0:
            counter += 1
            if counter == 4:
                print(number_str, end= " ")







