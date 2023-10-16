#28. Python program to print Fibonacci series using iteration
# Input the number of terms in the Fibonacci series

N = int(input("Enter the number whose you want to know series: "))

# Initialize the first two terms
a, b = 0, 1

# Print the first N terms of the Fibonacci series
if N <= 0:
    print("Please enter a another positive number except zero.")
elif N == 1:
    print(a)
else:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, N):
        a, b = b, a + b
        print(b, end=" ")
