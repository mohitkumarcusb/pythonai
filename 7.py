#7. Python program to find the geometric mean of n numbers
count= 0
product = 1.0
n = int(input("Enter the number of values: "))
while(count<n):
    x= float(input("Enter a real number: "))
    count = count+1
    product = product * x
    geometric_mean = pow(product,1.0/n)
print("The geometric mean is: ",geometric_mean)
