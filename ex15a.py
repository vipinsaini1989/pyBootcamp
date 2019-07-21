from sys import argv

script, filename = argv

file = open(filename)
file_data = file.read()
file.close()

print(f"Length of file '{filename}' is {len(file_data)} characters.")
