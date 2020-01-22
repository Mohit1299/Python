def is_prime(no):
    if(no < 2):
        print("Prime numbers are always greater than 2")
        return False
    count = 0
    for i in range(1,no):
        if(no%i==0):
            count += 1
        else:
            continue
    
    if(count == 1):
        return True
    else:
        return False
    
user_input = int(input("Enter the Number : "))
if(is_prime(user_input) == True):
    print("The number is Prime ")
else:  
    print("The number is Not Prime ")