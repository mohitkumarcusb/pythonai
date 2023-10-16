# 11. Python program to check whether the given integer is a prime number or not .

num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
    
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
