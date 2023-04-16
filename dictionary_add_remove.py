##    Adding an item to the dictionary is done by using
##    a new index key and assigning a value to it:
dict1 = {
    'key1' : 1,
    'key2' : 2,
    'key3' : 3
    }
print(dict1)
dict1['key4'] = 4
print(dict1)

##    The update() method will update the dictionary
##    with the items from a given argument. If the item
##    does not exist, the item will be added.

##    The argument must be a dictionary, or an
##    iterable object with key:value pairs.

dict1.update({'key5':5})
print(dict1)

dict1.pop('key1')
print(dict1)

##    The popitem() method removes the last inserted item
##    (in versions before 3.7, a random item is removed instead):

dict1.popitem()
print(dict1)

del dict1['key2']
print(dict1)

dict1.clear()
print(dict1)
