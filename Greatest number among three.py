x=int(input("enter first number"))
y=int(input("enter second number"))
z=int(input("enter third number"))

if(x>=y and x>=z):
    print("greatest number=",x)
elif(y>=x and y>=z):
    print("greatest number=",y)
    
else:
    print("greatest number =",z)
