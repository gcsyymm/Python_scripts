def f(fname):
    print(fname + 's')
f('hand')

##    Arguments are often shortened to args in Python documentations.

##    From a function's perspective:
##
##    A parameter is the variable listed inside the parentheses in the function definition.
##
##    An argument is the value that is sent to the function when it is called.

def combo(x,y):
    print(x,y,x+y)
combo(10,12)

##    If the number of arguments is unknown, add a * before the parameter name:
def low(*x):
    print(x[-1])
low(1,3,5,6)

##    Keyword Arguments are often shortened to kwargs
def gets(x1, x3, x2):
    print('the smallest value is' , x3)
gets(x3 = 10, x2 = 40, x1 = 100)
##    the order of the arguments does not matter.


def getx0(**xs):
    print('the value is ', xs['x0'])
##    the '' for x0 is necessary as the x0 is treated as string key here
getx0(x2 = 3, x1 = 10, y1 = 4, x0 = 1)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function()
##    the function will default think the input is a value rather than
##    key if the = is not in the input args, here the sweden represent
##    the 'Norway' value not the countru key

def f1(items):
    for i in items:
        print(i)
a = list(range(3))
f1(a)


