import sys
user_input = int(input("Enter the number"))
count = 1
for i in range(0,user_input):
    for j in range(0,i+1):
        if(count == user_input ):
            sys.exit()
        print(count,end="\t")
        count=count + 1
    print()