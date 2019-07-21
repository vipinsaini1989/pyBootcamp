from sys import argv

script, user_name = argv

print("hello,{user_name}")
print("what is you favourite subject?")
subject = input("> ")
print("what is your favourite food?")
food = input("> ")
print("what is your favourite sports?")
sport = input(">")
print("what is your favourite color?")
color = input(">")

print(f"""
Thanks {user_name} for the feedback. 
Below is your responses
    Subject: {subject}
    Food: {food}
    Sport: {sport}
    Color: {color}
""")

