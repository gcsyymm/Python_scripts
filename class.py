class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age) 

##    The self
##    Class methods must have an extra first parameter in the method definition
##    . We do not give a value for this parameter when we call the method,
##    Python provides it.
##    If we have a method that takes no arguments, we still have one argument.
##    This is similar to this pointer in C++ and this reference in Java.

##    When we call a method of this object as myobject.method(arg1, arg2),
##    this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)
##    – this is all the special self is about.


class char:
    x = 111
 # The init method or constructor
    def __init__(_, c_atk, c_def, c_hp):
        _.c_atk = c_atk
        _.c_def = c_def
        _.c_hp = c_hp
    def atk_buff(_, buff):
        _.buffed_atk = _.c_atk + buff
        return _.buffed_atk
 # Adds an instance variable
    def element(_, elm):
        _.elm = elm
        return _.elm
##    The __str__() function controls what should be returned
##    when the class object is represented as a string.
##
##    If the __str__() function is not set, the string representation of the
##    object is returned:  
    def __str__(_):
        return f'''ATK = {_.c_atk}\nDEF = {_.c_def} \nHP = {_.c_hp}'''
ganyu = char(100,80,130)
ganyu.c_atk += 10
a1 = ganyu_buff_atk = ganyu.atk_buff(100)
a2 = ganyu.x
print(a2)
print(f'Buffed ATK = {a1}')
print(ganyu,type(ganyu))
ganyu_Elm_type = ganyu.element('Cryro')
print(ganyu_Elm_type)

