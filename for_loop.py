list1 = list(range(10))
print(list1)
for x in list1:
    print(x)
    if x == 5:
        break

# list comprehension method
print([i for i in list1 if i <= 5])

##    this time break is before the print
for x in list1:
  if x == 5:
    break
  print(x)


##    Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!") 


##    Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") 
##    !!! Note: The else block will NOT be executed if
##    !!!       the loop is stopped by a break statement.


##    Nested Loops
list2 = list(range(3))
list3 = list(range(3,5))
for x in list2:
    for y in list3:
        print(x,y)

