# this can also be used to store data from multiple datatypes 
# tuple data type uses () parenthesi/round brackets to initialize data  

tuple = ('abcd', 786, 2.23, 'john', 70.2)

tinytuple = (123, 'john')

#prints the entire tuple 
print(tuple)

#prints the element in the tuple at index location 0
print(tuple[0])

#prints the elements from index location 1 till {3-1} = 2nd index location 
print(tuple[1:3])

#prints elements starting from the 3rd element, or the element situated at the index location number 2 in the initialized tuple 
print(tuple[2:])

#prints the tuple twice 
print(tinytuple * 2)

#prints the concatenated tuple
print(tuple + tinytuple)

#  A list can be updated
list = ['abcd', 786, 2.23, 'john', 70.2]
list[2] = 1000

# A Tuple can not be updated
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tuple[2] = 1000