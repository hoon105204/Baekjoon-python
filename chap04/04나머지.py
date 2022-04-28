myList=[]
for i in range(10):
    myList.append(int(input()))

for i in range(10):
    myList[i] = myList[i]%42

mySet = set(myList)
print(len(mySet))
