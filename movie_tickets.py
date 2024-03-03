ticket_count = input("How many tickets would you like to purchase: ")
ticket_count = int(ticket_count)
total_price = 0
count = 1
while ticket_count >= count:
    age = input(f"Please enter the age for ticket number {count}: ")
    count += 1
    age = int(age)
    if age >= 3 and age <= 12:
        total_price = total_price + 10
    elif age > 12:
        total_price = total_price +15    
print(f"The total price of the tickets is: ${total_price}")        
