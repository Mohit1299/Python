import sys

numbers = sys.argv[1:]

for x in range(0,len(numbers)):
    if(int(numbers[x]) % 2==0):
        print("",numbers[x])
