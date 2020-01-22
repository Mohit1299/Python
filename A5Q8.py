def unique_list(l):
    res = set(l)
    res = list(res)
    return res

user_input = input("Enter the elements in the list :")
user_input = list(map(int,user_input.strip().split(" ")))
print("The List with unique elements is : ",unique_list(user_input))