number = input("Enter a number and I'll tell you if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is divisible by 10")
else:
    print(f"The number {number} isn't divisible by 10")    
