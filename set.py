thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
##    Note: Sets are unordered, so you cannot be sure in which order the
##    items will appear.

##    Duplicates Not Allowed
##    Sets cannot have two items with the same value.

thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset2)
##    True and 1 is considered the same value:

##    The set() Constructor
##
##    It is also possible to use the set() constructor to make a set.
##    Example
##
##    Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) 
##    Check if "banana" is present in the set:
print("banana" in thisset) 


