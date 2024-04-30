length_cake = int(input())
width_cake = int(input())

total_pieces = length_cake * width_cake


while True:
    command = input()
    if command == "STOP":

        break
    else:
        command_int = int(command)

    total_pieces = total_pieces - command_int
    if total_pieces < 0:

        break

if total_pieces < 0:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")


"""length_cake = int(input())
width_cake = int(input())

total_pieces = length_cake * width_cake

command = input()
while command != "STOP":

    command_int = int(command)

    total_pieces = total_pieces - command_int
    if total_pieces < 0:
        print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
        break

    command = input()
else:
    print(f"{total_pieces} pieces are left.")



"""