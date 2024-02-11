guests = ['Carl Sagan', 'Glynn Johns', 'Steve Jobs', 'Philip Glass']

print(f"Dear {guests[0]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[1]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[2]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[3]}, you are formally invited to dinner on Friday February 9 at my house")
print("Good news everyone! I've found a bigger table and decided to invite some more guests")
guests.insert(0, 'David Bowie')
guests.insert(2, 'Barack Obama')
guests.append('Bernie Sanders')
guests.sort()
print(f"Dear {guests[0]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[1]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[2]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[3]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[4]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[5]}, you are formally invited to dinner on Friday February 9 at my house")
print(f"Dear {guests[6]}, you are formally invited to dinner on Friday February 9 at my house")
print("\nThe first three items in the list are:")
for guest in guests[:3]:
  print(guest)
print("\nThree items from the middle of the list are:")
for guest in guests[2:5]:
  print(guest)
print("\nThe last three items in the list are:")
for guest in guests[-3:]:
  print(guest)
