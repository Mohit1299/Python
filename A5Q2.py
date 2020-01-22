def sum_of_list(l):
    sum = 0
    for i in range(len(l)):
        sum += int(l[i])
    
    return sum 

user_input = input("Enter the numbers in the list : ")
user_input = user_input.split(" ")
print("The sum of elements in the list is : ",sum_of_list(user_input))