user_input = int(input("Enter the number to print tables : "))
for i in range(1,(user_input)+1):
    j=1
    while(j!=11):
        print(i*j ,end="\t")
        j=j+1
    print()