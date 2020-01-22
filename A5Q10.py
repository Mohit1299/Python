def even_list(l):
    res = []
    for i in range(0,(len(l))):
        if(l[i]%2==0):
            res.append(l[i])
        else:
            continue
                
    return list(set(res))

user_input = list(map(int,input("Enter the numbers of the list : ").strip().split(" ")))
print("The List with even numbers is : ",even_list(user_input))