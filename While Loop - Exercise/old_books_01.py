searched_book = input()
entered_book = input()

checked_book_qty = 0

while entered_book != searched_book:

    if entered_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {checked_book_qty} books.")
        break

    checked_book_qty += 1

    entered_book = input()
else:
    print(f"You checked {checked_book_qty} books and found it.")

    ///
    searched_book = input()

    checked_book_qty = 0

    while True:
        entered_book = input()

        if entered_book == searched_book:
            print(f"You checked {checked_book_qty} books and found it.")
            break

        if entered_book == "No More Books":
            print(f"The book you search is not here!")
            print(f"You checked {checked_book_qty} books.")
            break
        checked_book_qty += 1

///

