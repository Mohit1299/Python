def sort_alpha(str1):
    str1.sort()
    print("The alphabetically sorted string is : ")
    for i in range(len(str1)):
        print(str1[i],end="-")

user_input = input("Enter the string : ")
sort_alpha(user_input.split("-"))