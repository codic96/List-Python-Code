#Reversing a list using reversed()

def reverse(lst):
    return [ele for ele in reversed(lst)]


#Driver Code
lst = [10,13,13,133,1330,18]
print(reverse(lst))

#Method 2: using the reverse() built in function.

#Reversing a list using reverse function

def Reverse(lst):
    lst.reverse()
    return lst

#Driver Code
lst = [10,11,12,13,14,15]
print(Reverse(lst))
       
