def input_no():
    no = int(input("Enter Number : "))
    if(no<=0):
        print("You have enter a non-positive Number.Please enter positive Number")
        input_no()
    else:
        sum = 0
        for i in range(1,no+1):
            sum+=i
        print(sum)

if __name__ == "__main__":
    input_no()




