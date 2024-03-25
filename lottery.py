from random import choice
lotto_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
lotto_letters = ('a', 'b', 'c', 'd', 'e')
winning_number = (f"{choice(lotto_digits)}{choice(lotto_digits)}"
                  f"{choice(lotto_digits)}{choice(lotto_digits)}"
                  f"{choice(lotto_letters)}")

user_ticket = input("Please input your lottery ticket number containing 4 "
                    "numbers and 1 letter: ")

if user_ticket == winning_number:
    print("Congratulations! You are a winner!")
else:
    print("Better luck next time :(")
