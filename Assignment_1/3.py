#3 Python program to find the product of a set of real numbers.


x=int(input("enter the number you want to product:-"))
product=1
for i in range(x):
    z=float(input("enter the numbers:-"))
    product=product*z
print("the product is :",product)

