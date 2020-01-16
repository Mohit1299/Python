import copy
import itertools
s1 = set(range(1,10))
s2 = set(range(15,20))

#Intial Set 
print("The initial Set S1 is : ",s1)
print("The initial Set S2 is : ",s2)


print("\n")
#Shallow and Deep Copy
s3 = copy.deepcopy(s1)
s4 = copy.copy(s2)
s4.add(9)
s3.add(16)
print(s1)
print(s2)
print("The deep copy of s1 is s3 : ",s3)
print("The shallow copy of s2 is s4 : ",s4)


print("\n")
#Appending and extending of a set
s4.update(range(20,25))
s4.update(range(30,35))

print("The set s4 after updating is : ",s4)

print("\n")
#remove and pop 
s3.remove(5)
print("The set S3 after removing 5 : ",s3)
s4.pop()
print("The set s3 after poping : ",s3)


print("\n")
#adding and inserting
s3.update(set(itertools.islice(s4,5)))
#s3.update(s4[1:4])

print(s3)