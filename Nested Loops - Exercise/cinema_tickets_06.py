movie_name = input()
left_seats = 0
student_tickets = 0
standart_tickets = 0
kids_tickets = 0
total_movie_tickets = 0

while movie_name != "Finish":
    free_seats = int(input())
    ticket_type = input()

    left_seats = 0
    total_tickets = 0

    while ticket_type != "End":
        left_seats += 1
        total_movie_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standart_tickets += 1
        elif ticket_type =="kid":
            kids_tickets += 1

        if left_seats == free_seats:
            break


        ticket_type = input()

    print(f"{movie_name} - {left_seats / free_seats * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_movie_tickets}")
print(f"{student_tickets/total_movie_tickets * 100:.2f}% student tickets.")
print(f"{standart_tickets/total_movie_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets/total_movie_tickets * 100:.2f}% kids tickets.")