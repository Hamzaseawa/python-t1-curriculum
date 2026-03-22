fruits = ["apple","bannana","cherry"]

# find if apple is in the list
if "apple" in fruits:
    print("found apple.")
else:
    print("apple not found.")


found = False 
index = -1

for i in range(len(fruits)):  # Looping through the list
    if fruits[i] == "apple":
        found = True
        index = i
        break 

    if found == True:
        print("found apple.")
    else:
        print("no apples in list.")
    