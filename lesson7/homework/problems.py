# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total = 0
for i in range (len(numbers)):
    item = numbers[i]
    if item > 25 :
        total += item #total = total + item
print(total)
# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
total = 0
for i in range (len(numbers)):
    item = numbers[i]
    if item < -10 :
        total += item
print(total)
# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
biggest_item = -float("inf")
for i in range (len(numbers)):
    item = numbers[i]
    if item < 100 :
        if biggest_item < item :
            biggest_item = item
print("the biggest item in the list is: ", biggest_item)
# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest_item = -float("inf")
for i in range (len(numbers)):
    item = numbers[i]
    if item > biggest_item:
        biggest_item = item
print("the biggest number is:",biggest_item)
# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
total = sum(numbers)
print(total)