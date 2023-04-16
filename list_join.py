##Join Two Lists
##
##There are several ways to join, or concatenate, two or more lists in Python.
##
##One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 

##append method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1) 


##extend method
list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]

list3.extend(list4)
print(list3) 


##    append()	Adds an element at the end of the list
##    clear()	Removes all the elements from the list
##    copy()	Returns a copy of the list
##    count()	Returns the number of elements with the specified value
##    extend()	Add the elements of a list (or any iterable), to the end of the current list
##    index()	Returns the index of the first element with the specified value
##    insert()	Adds an element at the specified position
##    pop()	Removes the element at the specified position
##    remove()	Removes the item with the specified value
##    reverse()	Reverses the order of the list
##    sort()	Sorts the list
