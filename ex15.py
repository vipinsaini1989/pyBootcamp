from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is your {filename}:")
print(txt.read())

print(f"print filename:")
file = input(">")

file_again = open(file)
print(file_again.read())
file_again.close()