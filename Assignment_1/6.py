#6 Python program to display the given integer in a reverse manner.
x=int(input("enter the number:-"))
rev=0
while(x!=0):
    y=x%10
    rev=(rev*10)+y
    x=x//10
print("reverse manner of given integer=",rev)


