#14. Python program to print the numbers from a given number n till 0 using recursion
n = int(input("enter the numbers:-"))

def rec(n):
    if n==0:
        print(0)
    else:
        print(n)
        rec(n-1)
        

rec(n)
