##    To create a tuple with only one item, you have to add a
##    comma after the item, otherwise Python will
##    not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple, it is a string
thistuple = ("apple")
print(type(thistuple)) 

thistuple = tuple('apple')
print(type(thistuple)) 
