rivers = {
    'amazon': 'brazil',
    'seine': 'france',
    'volga': 'russia',
    }
for river, country in rivers.items():
    print(f"The {river.title()} is a river that runs through {country.title()}")
for river in rivers:
    print(river.title())    
for country in rivers.values():
    print(country.title())
