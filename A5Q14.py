def is_panagram(str1):
    flag=0
    str1 = str1.lower()
    res_set = set(str1)
    chars = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(chars)):
        if(chars[i] in res_set):
            flag = 1
        else:
            flag = 0
            break

    if(flag == 1):
        print("Entered String is Panagram")
    else:
        print("Entered String is not a Panagram")
user_input = input("Enter the string : ")
is_panagram(user_input)