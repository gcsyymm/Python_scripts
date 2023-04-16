dict1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
    }
##    Make a copy of a dictionary with the copy() method:
dict1_copy = dict1.copy()
print(dict1_copy)

##    Another way to make a copy is to use the built-in function dict().
dict1_du = dict(dict1)
print(dict1_du)


dict2 = {
    'd' : 4
    }

dict3 = {
    'e' : 5
    }

nested_dict = {
    'dict1' : dict1,
    'dict2' : dict2,
    'dict3' : dict3,
    }
print(nested_dict)

##    To access items from a nested dictionary, you use the name of the
##    dictionaries, starting with the outer dictionary:
print(nested_dict['dict1']['a'])
print(nested_dict['dict1'])


Dictionary Methods

##    Python has a set of built-in methods that you can use on dictionaries.
##    Method 	Description
##    clear()	Removes all the elements from the dictionary
##    copy()	Returns a copy of the dictionary
##    fromkeys()	Returns a dictionary with the specified keys and value
##    get()	Returns the value of the specified key
##    items()	Returns a list containing a tuple for each key value pair
##    keys()	Returns a list containing the dictionary's keys
##    pop()	Removes the element with the specified key
##    popitem()	Removes the last inserted key-value pair
##    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
##    update()	Updates the dictionary with the specified key-value pairs
##    values()	Returns a list of all the values in the dictionary 
