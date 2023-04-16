## without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

## with list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


## Syntax is
##    newlist = [expression for item in iterable if condition == True]

##  Condition
##  The condition is like a filter that only accepts the items that valuate to True.

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

##Expression
##
##  The expression is the current item in the iteration,
##  but it is also the outcome, which you can manipulate before
##  it ends up like a list item in the new list:

##Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits] 
print(newlist)

##Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

##Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

##!!! The expression in the example above says:
##
## "Return the item if it is not banana, if it is banana return orange".

