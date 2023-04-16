set1 = set(range(3))
set2 = set(range(1,6))
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

##    Note: Both union() and update() will exclude any duplicate items.

##    Keep ONLY the Duplicates
##    The intersection_update() method will keep only
##    the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x) 

##    The intersection() method will return a new set,
##    that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z) 


##    Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) 

##    The symmetric_difference() method will return a new set,
##    that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) 

##     The values True and 1 are considered the same value in sets,
##     and are treated as duplicates:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)

