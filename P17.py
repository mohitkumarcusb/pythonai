#17. Python program to implement linear search
print("Enter 15 Numbers: ")
arr = []
for i in range(15):
  arr.insert(i, int(input()))
print("Enter the Number to Search: ")
num = int(input())
for i in range(15):
  if num==arr[i]:
    index = i
    break
print("\nNumber Found at Index Number: ")
print(index)
