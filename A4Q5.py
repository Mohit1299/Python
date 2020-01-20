user_input = input("Enter the comma separated values : ")

user_input = user_input.split(",")

sum = 0

for i in range(0,len(user_input)):
    sum += (int(user_input[i]))

print(sum)