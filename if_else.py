##    This technique is known as Ternary Operators, or Conditional Expressions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 
print("A" if a > b else "=" if a == b else "B") 

##    Nested If
##
##    You can have if statements inside if statements, this
##    is called nested if statements.

x = 80
if x > 60:
    print('Good')
    if x >= 80:
        print('Really!')
else:
    print('Not good')
    
