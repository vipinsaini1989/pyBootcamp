from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print(f"If you don't want press, CTRL + C")
print("If you do want, hit ENTER")

input("?")

print("opening the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye")
target.truncate()

print("Now I am going to ask three line")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these line to file")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("Finally, closing the file")
target.close()