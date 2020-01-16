import copy

print("\n")
#creating list
l1 = list(range(1,10))

l2 = list(range(15,20))

print("The list L1 is : ",l1)
print("The list L2 is : ",l2)


print("\n")
#creating Shallow and deep copy
l3 = copy.deepcopy(l1)

l4 = copy.copy(l2)


print("The list L3 is (deep copy of L1) : ",l3)

print("The list L4 is (shallow copy of L2) : ",l4)


print("\n")
#appending the list
print("The List L4 before appending 20-25 : ",l4)
print("The List L3 before extending 30-35 : ",l3)

l4.append(list(range(20,25)))
l3.extend(list(range(30,35)))

print("The List L4 after appending 20-25 : ",l4)
print("The List L3 after extending 30-35 : ",l3)


print("\n")
#remove 
print("The list L3(before removing 2) : ",l3)
l3.remove(2)
print("The list L3 (after removing 2) : ",l3)


print("\n")
#pop

print("The List L4 (before popping : )",l4)
l4.pop(2)
print("The List L4 (after popping : )",l4)


print("\n")
l3.insert(1,l4[1])
print("List after inserting first index element of L4 in L3",l3)

print("\n")
l3[2:5] = [99,98,97]

print("List L3 after adding 97,98,99 : ",l3)