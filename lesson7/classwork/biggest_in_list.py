numbers = [1,2,3,4,5,6]
print(numbers)

# You can use built-in Python functions to find the biggest and smallest numbers in a list
biggest_item = max(numbers) # max is maximum
smallest_item = min(numbers) # min is minimum

print("the biggest item in the list is: ", biggest_item)
print("the smallest item in the list is: ", smallest_item)

print("our algorithm: ")

biggest = numbers[0] # start by assuming the first item is the biggest
for i in range(len(numbers)):
    if numbers[i] > biggest:
        biggest = numbers[i]
print("the biggest item in the list is: ", biggest_item)