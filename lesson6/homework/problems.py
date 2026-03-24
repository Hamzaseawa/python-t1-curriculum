# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
counter = 0
for i in range (len(names)):
    item = names[i]
    if item == "Alex":
        counter = counter +1
print(counter)
# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
found = False 
for i in range (len(animals)):
    item = animals[i]
    if item == "elephant":
       found = True
       break
if found == True:
    print("elephant found.")
else:
    print("elephant not found.")
# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
counter = 0
for i in range (len(scores)):
    item = scores[i]
    if item == 100:
        counter = counter +1
print(counter)
# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
index = -1
found = False
for i in range (len(colors)):
    item = colors[i]
    if item == "blue":
       found = True
       index = i
       break
if found == True:
    print(index)
else:
    print("blue not found.")
# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
counter = 0
for i in range(len(temperatures)):
    item = temperatures[i]
    if item < 0:
        counter = counter +1
print(counter)