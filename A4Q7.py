user_str = input("Enter the string : ")
user_input = user_str.split(" ")
dict = {}
for i in range(0,len(user_input)):
    if user_input[i] in dict.keys():
        dict[user_input[i]] = dict[user_input[i]] + 1
    else:
        dict[user_input[i]] = 1

print(dict)