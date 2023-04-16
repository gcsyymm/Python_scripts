list1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list1.sort()
print(list1)
list2 = [100, 50, 65, 82, 23]
list2.sort(reverse = True)
print(list2)

def key(x):
    return abs(x-50)
list2.sort(key = key)
print(list2)

## Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.upper)
print(thislist)

## The reverse() method reverses the current sorting order of the elements.
thislist.reverse()
print(thislist)
