''' Different ways to clear a list in Python '''

#Method1

#Python program to clear a list
#Using clear() method

#Creating list

GEEK = [16,0,4,1]
print('GEEK before clear:',GEEK)

#clearing list
GEEK.clear()
print('Geek after clear',GEEK)


#Method 2 : Reinitializing the list: The initializing of the list in that scope,initializes the list with no value.

#initializing lists

list1 = [1,2,3,4]
list2 = [5,6,7,8]

#Printing list1 before deleting lists
print("List1 before deleting is"+str(list1))
#deleting list using clear()

list1.clear()
