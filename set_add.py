##    Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

##    Add Sets
##    To add items from another set into the current set,
##    use the update() method.
##    Example
##    Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

##    Add Any Iterable
##    The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
##    Example
##    Add elements of a list to at set:

thisset2 = {"apple", "banana", "cherry"}

mylist = ["kiwi", "orange"]

thisset2.update(mylist)

print(thisset2)

################################################################

##    Remove "banana" by using the remove() method:
thisset3 = {"apple", "banana", "cherry"}

thisset3.remove("banana")

print(thisset3)


##    !!!Note: If the item to remove does not exist, remove() will raise an error.

##    Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

##   !!! Note: If the item to remove does not exist,
##    discard() will NOT raise an error.


##    Remove a random item by using the pop() method:
thisset4 = {"apple", "banana", "cherry"}

x = thisset4.pop()

print(x)

print(thisset4) 
