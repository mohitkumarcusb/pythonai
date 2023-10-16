list = []
a = int(input('How many numbers you want to insert into list: '))
for n in range(a):
    x = int(input('Enter number '))
    list.append(x)
print("Sum of numbers in the given list is :", sum(list))
