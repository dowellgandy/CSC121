sandwich_orders = ['turkey', 'tuna', 'blt', 'italian']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"We are making your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)
print("We made the following sandwiches:")    
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich} sandwich")
