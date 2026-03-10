list1 = ['physics', 'chemistry', 1997, 2000]

#any type of data can be stored, we just need to place those comma seperated data in square brackets

print('List1[0]: ', list1[0]) #fetched item from index 0
print('List1[1:5]: ', list1[1:5]) #fetched items from index 0 till index 1 till index 4

#updating a value in a list
print(list1[2])

list1[2] = 2005

print(list1[2])

#deleting an item from a list 

print("Before deletion: ", list1)

del list1[2]

print("After deleting an item from the list: ", list1)