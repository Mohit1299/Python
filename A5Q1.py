def max(a,b,c): 
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

no1 = int(input("Enter number : "))
no2 = int(input("Enter number : "))
no3 = int(input("Enter number : "))

print("The maximum number is : ",max(no1,no2,no3))