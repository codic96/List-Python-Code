#Python3 program to swap first and last element of a list

#Swap function

def swapList(newList):
    size = len(newList)

    #Swapping
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

#Driver code

newList = [12,13,14,122]
print(swapList(newList))
