def outer():
    def input_no():
        user_input = int(input("Enter the Number :"))
        if(user_input < 0):
            print("Please Enter Positive Number ")
            input_no()
        else:
            is_perfect(user_input)
    
    def is_perfect(no):
        divisors = []
        for i in range(1,no):
            if(no%i==0):
                divisors.append(i)
            else:
                continue
        sum = 0
        for i in range(len(divisors)):
            sum += divisors[i]
  
        if(sum == no) :
            print("The number is a perfect Number ")
        else:
            print("The number is not a perfect Number ")

    input_no()


outer()
