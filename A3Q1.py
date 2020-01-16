input_year = int(input("Enter Year : "))

if(((input_year%4==0)and(input_year%100==0)and(input_year%400==0))or((input_year%4==0)and(input_year%100!=0))):
    print("leap Year")
else:
    print("Not a Leap Year")