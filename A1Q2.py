#user input
str1 = input("Enter the first string : ")
str2 = input("Enter the Second string : ")
str1=str1.strip()
str2=str2.strip()

print("\n")
#concating the strings
str3 = str1+str2
#str3 = "%s%s"%(str1,str2)
#str3 = "{}{}".format(str1,str2)
#str3 = f'{str1}{str2}'
#print("".join([str1,str2]))
print(str3)


print("\n")
#converting to upper case
print("The Upper case is : ",str3.upper())


print("\n")
#converting to lower case
print("The Lower case is : ",str3.lower())


print("\n")
#converting to title case
print("The Title case is : ",str3.title())




print("\n")
#spliting the string 
str1_len = len(str1)
str4 =""
str4 += str3[:str1_len]
print(str4)


print("\n")
#formating string to center 
print(str4.center(30,'$'))