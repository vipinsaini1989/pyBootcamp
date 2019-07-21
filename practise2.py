from sys import argv

script,name,city,profession,age = argv

# print("Hi, I am a bio-generator")
# name = input("what is your name: ")
# city = input("where are you from: ")
# profession = input("what is your profession: ")
# age = int(input("what is your age: "))

print(f"""
    Hello, My name is {name}
    I am from {city}
    My profession is {profession}
    My age is {age}
    so, i was born in {2019 - int(age)}
""")