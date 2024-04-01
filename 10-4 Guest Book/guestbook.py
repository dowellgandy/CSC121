from pathlib import Path

print("Enter your name to be added to the guest book")
print("Press enter to quit")

name = True
guestList = ''
path = Path('guest_book.txt')

while name:
    name = input("Name: ")
    if name:
        print(f"Welcome {name}, your name will be added to the guest book")
    else:
        print("Thank you, goodbye!")
    guestList += (f"{name}\n")
    path.write_text(guestList)

