# the list method we are going to learn in this section 


# ✅ Quick List of All Important Methods
# Method	Description
# append(x)	Add element at end
# extend(iterable)	Add multiple elements at end
# insert(i, x)	Insert element at given index
# remove(x)	Remove first occurrence of element
# pop([i])	Remove and return element at index (default last)
# clear()	Remove all items
# index(x)	Return index of first occurrence
# count(x)	Count occurrences
# sort()	Sort list (ascending by default)
# reverse()	Reverse the list
# copy()	Shallow copy of list


friend = ['joy','bob','alias', 45.2, 45, False, "Apple"]

print(friend)   # this print first element of the list 



friend.append("sugriv")  # at the end of the list it will be going to add 

print(friend)

l1 = [112, 108, 56,89,98,67,87,57]




# l1.sort() # this sort the content osrting the list 
# l1.reverse() # it will reverse the list last to first

 # sytanx for the inserting [index_number, index_that_need_to_add]
 
# l1.insert(2,333333333)  # this will add the 33333 to 2 nd number in the list and list always start from 0

print(l1.pop(2))
remove3 = l1.pop(2)



print(remove3)


l1.remove(112)



print(l1)