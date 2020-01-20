first_number = int(input("Enter the first number : "))
second_number =  int(input("Enter the second number : "))

def gcd(first_number,second_number):
    if(second_number == 0):
        return first_number
    return gcd(second_number,first_number%second_number)
    
res = gcd(first_number,second_number)
print(res)