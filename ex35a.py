def greeting(name):
    print(f'welcome {name}, Which seat do you want to prefer?')
    print('''
        1 ---> First Room
        2 ---> Second Room
        3 ---> Third Room
        4 ---> Forth Room
        5 ---> In Hall
    '''
          )
    user_input = input(">")

    if user_input:
        print(f"You are assigned: {user_input}")
        print("Thanks for coming! Enjoy the day!")
    else:
        greeting(name)


def askName():
    name = input(">")

    if name and name.lower() != 'no':
        title_case_name = name.title()
        greeting(title_case_name)

    else:
        askName()


def start():
    print("Hello, welcome to Jaaga. May I know you name?")
    askName()


start()
