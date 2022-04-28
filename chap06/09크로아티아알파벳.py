myList = ["c=","c-","dz=","d-","lj","nj","s=","z="]
inputString = input()

for i in myList:
    if i in inputString:
        inputString = inputString.replace(i,"0")

print(len(inputString))