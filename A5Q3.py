def mul_of_list(l):
    mul = 1
    for i in range(len(l)):
        mul *= int(l[i])

    return mul

user_input = input("Enter the elements in a list : ")
user_input = user_input.split(" ") 
print("The product of elements in a List is :",mul_of_list(user_input))