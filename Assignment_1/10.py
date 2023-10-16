#10. Python program to display all integers within the range 100 -200 whose sum of digits is an even number.
print("all integers within the range 100 -200 whose sum of digits is an even number:-")
for i in range(100,200):
    summ=0
    temp=i
    while(temp!=0):
        
        digit=temp%10
        summ=summ+digit
        temp=temp//10
    if (summ%2==0):
        print(i)
    
