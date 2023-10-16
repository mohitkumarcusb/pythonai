#13. Python program to find the roots of a quadratic equation

from math import sqrt

print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("The roots are: %f ",x1)
    print("The roots are: %f ",x2)
    
elif r == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("There is one root: ", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0.")
    exit()
