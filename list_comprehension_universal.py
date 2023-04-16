list1=[0,1,2,3,4,5,6,7,8,9,10]
list2=[x**2 if x == 5 else '' if x>7 else x for x in list1 if x > 2 or x == 0]

print(list2)
print(type(list[-1]))
