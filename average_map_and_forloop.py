file = input("Enter input file name: ")

f = open(file,'r')
numStringList = f.readlines()
f.close()

numString = ""
for eachStringItem in numStringList:
    numString = numString + eachStringItem
    numList = numString.split()
numList = list(map(float,numList))

newNumList = []
for eachListItem in numList:
    eachListItem = float(eachListItem)
    newNumList.append(eachListItem)


print("")
print(numStringList)
print("")
print(numString)
print("")
print(numList)
print("")
print(newNumList)



