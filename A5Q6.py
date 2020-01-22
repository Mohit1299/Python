def in_range(no,start,end):
    flag = 0
    for i in range(start,end):
        if(no==i):
            flag=1
    
    return flag

input_no = int(input("Enter the number to find in a range :"))
input_range = input("Enter the range : ")
input_range = input_range.split(" ")
 
if( in_range(input_no,int(input_range[0]),int(input_range[1]))== 1):
    print("The number is in the range")
else:
    print("The number is not in the range")