dict1 = {
    'key1' : 1,
    'key2' : 2,
    'key3' : 3
    }
##    Print all key names
for x in dict1:
    print(x)

for x in dict1.keys():
    print(x)

    
##    Print all values
for x in dict1:
    print(dict1[x])

for x in dict1.values():
    print(x)

##    Loop through both keys and values, by using the items() method:
for x in dict1.items():
    print(x)

for x, y in dict1.items():
    print(x, y)
