def describe_city(city_name, country_name='france'):
    """Display information about a city"""
    print(f"{city_name.title()} is in {country_name.title()}")

describe_city(city_name='paris')

describe_city(city_name='nice')

describe_city(city_name='berlin', country_name='germany')
