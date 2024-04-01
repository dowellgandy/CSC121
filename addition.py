print("Enter two numbers to add them")
print("Enter q to quit")

while True:

    number1 = input("Number 1: ")
    if number1.lower() == 'q':
        break
    number2 = input("Number 2: ")
    if number2.lower() == 'q':
        break

    try:
        answer = int(number1) + int(number2)
        print(answer)
    except ValueError:
        print("Please enter numbers. Not text")
