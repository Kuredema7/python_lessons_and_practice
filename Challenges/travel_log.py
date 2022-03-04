travel_log = [
    {
        "country": 'France',
        "visits": 12,
        "cities": ['Paris', 'Lille', 'Dijon']
    },
    {
        "country": 'Germany',
        "visits": 5,
        "cities": ['Berlin', 'Hamburg', 'Stuttgart']
    }
]

def add_new_country(country_name, no_of_visits, list_of_cities):
    travel_log.append({"country": country_name, "visits": no_of_visits, "cities": list_of_cities})

add_new_country("Russia", 2, ['Moscow', 'Sain Peterburg'])
print(travel_log)