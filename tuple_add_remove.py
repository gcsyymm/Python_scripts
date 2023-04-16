##    Add tuple to a tuple. You are allowed to add tuples to tuples,
##    so if you want to add one item, (or many), create a new tuple with
##    the item(s), and add it to the existing tuple:
##    Example
##
##    Create a new tuple with the value "orange", and add that tuple:

tuple1 = tuple(range(10))
tuple2 = tuple(range(11,20))
tuple1 += tuple2
print(tuple1)


##    Tuples are unchangeable, so you cannot remove
##    items from it, but you can use the same workaround as
##    we used for changing and adding tuple items:
##    Example
##    Convert the tuple into a list, remove "apple",
##    and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
