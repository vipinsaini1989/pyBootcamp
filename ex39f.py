user_input = int(input("Enter the number of time you want print '@': "))

for i in range(1, user_input):
    print(' ' * (user_input-(i+1)) + '@'*i)

skip = 0
while user_input:
    print(" " * skip + "*" * user_input)
    user_input -= 1
    skip += 1

n = 3
for i in range(n):
    # print("#" * i + '\\')
    skip = n-i-1
    print(i, skip)
    # print(' ' * skip + '/'+" " * i + '\\')
