user_info = {}

for num in range(1):
    name = input("Enter your name: ")
    english = input("How much you score in English: ")
    science = input("How much you score in science: ")
    maths = input("How much you score in maths: ")

    marks = {}
    marks['English'] = english
    marks['Science'] = science
    marks['Maths'] = maths
    user_info[name] = marks

print(user_info)
