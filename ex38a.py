name = input("Enter names: ")

name_list = name.split()
name_length_list = []

for name in name_list:
    name_length = len(name)
    name_length_list.append(name_length)

print(name_length_list)
