def is_palindrome(str1):
    res_str = ""
    for i in range(len(str1)):
        res_str = res_str + str1[i]
    if(res_str == res_str[::-1]):
        print("The Entered string is Palindrome")
    else:
        print("The Entered string is not a Palindrome")


user_input = input("Enter the String : ")
is_palindrome(user_input.strip().split(" "))