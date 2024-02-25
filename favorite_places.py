favorite_places = {
    'john': ['aruba'],
    'mark': ['florida', 'paris'],
    'tony': ['charleston', 'san francisco', 'mexico city'],
    'philip': [],
    }
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(place.title())
    elif len(places) == 1:
        print(f"{name.title()}'s favorite place is:")
        for place in places:
            print(place.title())
    else:
        print(f"\n{name.title()} doesn't have any favorite places")
                



