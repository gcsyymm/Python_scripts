thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)

x = thisdict.get('model')
print(x)

##    Get a list of the keys:
x = thisdict.keys()
print(x,type(x))

##    Get a list of the values:
y = thisdict.values()
print(y,type(y))

##    Get a list of the key:value pairs
z = thisdict.items()
print(z,type(z))

##    Check if Key Exists
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
