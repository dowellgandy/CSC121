def make_car(make, model, **car_info):
    """Store information about a car in a dictionary"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'crosstrek', color='white', roof_rack=True, year=2015)

print(car)
