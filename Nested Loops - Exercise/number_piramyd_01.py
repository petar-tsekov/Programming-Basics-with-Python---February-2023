n = int(input())
currend_num = 1
is_found = False
for x in range(1 ,n+1):
    for y in range(1, x+1):
        print(currend_num, end=" ")
        currend_num += 1
        if currend_num == n + 1:
            is_found = True
            break
    print()

    if is_found:
        break