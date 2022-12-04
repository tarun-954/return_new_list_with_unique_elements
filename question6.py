def getUniqueElements(numList):
    unique = []
    for i in numList:
        if i not in unique:
            unique.append(i)
    
    print(unique)
    
numbersList = [1, 2, 5, 2, 5, 1, 3, 7, 9]

getUniqueElements(numbersList)


