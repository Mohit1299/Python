def reverse_string(str1):
    res_str = ""
    res_str += str1[::-1]
    return res_str

user_input = input("Enter the string : ")
print("The Reverse of the String is :",reverse_string(user_input))