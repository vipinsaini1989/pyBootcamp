user_information = []

for number in range(3):
    name = input("Enter your name: ")
    age = input(f"{name.title()}, enter your age: ")
    city = input(f"{name.title()}, enter your city: ")
    pincode = input(f"{name.title()}, enter your city pincode: ")

    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['city'] = city
    user_info['zipcode'] = pincode
    user_information.append(user_info)

print("Name Age City Zipcode")
print("-"*30)

for user in user_information:
    print(
        f"{user['name']}  {user['age']}   {user['city']}  {user['zipcode']}")
