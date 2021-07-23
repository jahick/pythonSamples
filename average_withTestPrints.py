from functools import reduce
import math

file = input("Enter input file name: ")


f = open(file,'r')
numStringList = f.readlines()
f.close()


numString = ""
for eachStringItem in numStringList:
    numString = numString + eachStringItem
    numList = numString.split()


numList = list(map(float,numList))

addition = reduce(lambda x,y: x + y, numList)

if len(numList) == 0:
    average = 0
else:
    average = addition / len(numList)


print("")
print(numStringList)
print("")
print(numString)
print("")
print(numList)
print("")
print(addition)
print("")
print("The average is",average)



