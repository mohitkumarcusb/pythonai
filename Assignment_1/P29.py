#29. Python program to print all the items in a dictionary. 
# Input a dictionary

thisdict = {"Name": "Mohit", "Age": 23, "City": "Gaya"}

# Print all items in the dictionary

for key, value in thisdict.items():
    print(f"{key}: {value}")
