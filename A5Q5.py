def factorial(no) :
    fact = 1
    if(no == 0):
        return fact
    else:
        for i in range(no,1,-1):
            fact *= i
        return fact

def input_function():
    user_input = int(input("Enter the non-negative integer : "))
    if(user_input<0):
        print("You have entered negative integer.")
        input_function()
    else:
        print("The factorial of the number is : ",factorial(user_input))

if __name__ == "__main__":
    input_function()