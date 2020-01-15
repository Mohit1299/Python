#user input
first_name = input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
user_age = int(input("Enter your Age : "))
user_salary = int(input("Enter your Salary : "))
first_name = first_name.strip()
last_name = last_name.strip()

print("\n")
#two string joining
user_name = first_name+last_name
#user_name = "%s%s"%(first_name,last_name)
#user_name = "{}{}".format(first_name,last_name)
#user_name = f'{first_name}{last_name}'
#print("".join([first_name,last_name]))
print(user_name)


print("\n")
#character at position 3
print("Character at Index Position 3")
print(first_name[3])
print(last_name[3])


print("\n")
#character at position -3
print("Character at Index Positon -3")
print(first_name[-3])
print(last_name[-3])


print("\n")
#Binary Conversion of Integers
print("The binary conversion Integers")
print(format(user_age,"b"))
print(format(user_salary,"b"))


print("\n")
#Class of the user input
print("The class of the user input ")
print("The Class of User_Name is : ",type(user_name))
print("The class of User_Age is : ",type(user_age))
print("The class of User_Salary : ",type(user_salary))


print("\n")
#order of the character at index 1
first_name_order = ord(first_name[1])
last_name_order = ord(last_name[1])
print("The order of first element of string is : ",first_name_order)
print("The order of last element of string is : ",last_name_order)