def count_upper_lower(str1):
    uppercase = 0
    lowercase = 0
    result = []
    for i in range(len(str1)):
        if(str1[i].isupper()):
            uppercase += 1
        elif(str1[i].islower()):
            lowercase += 1
        else:
            continue
    result = [uppercase,lowercase]        
    return result

user_input = input("Enter the String : ")
result = []
result = count_upper_lower(user_input)
print("The Number of Uppercase letters is : ",result[0])
print("The number of Lowercase letters is : ",result[1])