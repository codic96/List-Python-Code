
#Python program to find sum of elements in list

#Python program to find sum of elements in list

total =0

#Changing a list
list1 = [11,5,17,18,23]
#Iterate each element in list
#and add them in variable total

for ele in range(0,len(list1)):
    total = total + list1[ele]

#printing total value
print("Sum of all element in give list:",total)
    