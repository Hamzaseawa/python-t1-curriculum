numbers = [5, -8, 35, -3, 6, 2]

t                               
print("the sum is:", total)

print("our algorthim:")

total2 = 0
for i in range(len(numbers)):
    item = numbers[i]
    total2 = total2 + item
print("the sum is:", total2)

# find the sum of only the positive numbers.

total3 = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 0:
        total3 = total3 + item
print("the sum of only the positive numbers is:", total3)