first_no = int(input("Enter the first No : "))
second_no = int(input("Enter the second No : "))

print("The input numbers are : ",first_no,second_no)

print("\n")
#binary Conversion
print("The binary conversion of the first No is : ",bin(first_no))
print("The binary conversion of the second No is : ",bin(second_no))


print("\n")
#Operation using And OR XOR
print("The result of and operation is : ",first_no & second_no)
print("The result of or operation is : ",first_no | second_no)
print("The result of Xor operation is : ",first_no ^ second_no)


print("\n")
#operation using comparison operator
print("The result of (==) comparison operator is : ",first_no==second_no)
print("The result of (!=) comparison operator is : ",first_no!=second_no)
print("The result of (>=) comparison operator is : ",first_no>=second_no)
print("The result of (<=) comparison operator is : ",first_no<=second_no)
#print("The result of (<>) comaprison operator is : ",first_no<>second_no)
print("The result of (> ) comparison operator is : ",first_no>second_no)
print("The result of (< ) comparison operator is : ",first_no<second_no)


print("\n")
#left and right shift
print("The first_no after being left shift by 4 is : ",first_no<<4)
print("The second_no after being right shift by 3 is :",second_no>>3)
