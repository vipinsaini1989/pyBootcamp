name_and_age = {}
name_and_city = {}

for number in range(1):
    name = input("Enter name: ")
    age = input(f"Enter age of {name}: ")
    city = input("Can tell me the city: ")

    name_and_age[name] = age
    name_and_city[name] = city.title()


name_key = input("Enter the name of person you want to know: ")

print(f"""
    Age: {name_and_age[name_key]}
    City: {name_and_city[name_key]}
""")
