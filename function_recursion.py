def f(x):
  if x > 0:
    result = x + f(x - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
print(f(3))

##    calls proceed
##    result = 3 + f(2)
##    result = 2 + f(1)
##    result = 1 + f(0) = 1 + 0
##    returning proceed
##    result = 1 = 1
##    result = 2 + 1 = 3
##    result = 3 + 2 + 1 = 6

def f1(x):
  if x > 0:
    result = x + f1(x - 1)
    print(result)
  else:
    return 0
  return result

print("\n\nRecursion Example Results")
print(f1(3))
