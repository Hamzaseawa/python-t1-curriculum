# Problem 1
# Write a function that returns the number 42 and print the result.
def king_return():
    return 42
num = king_return()
print(num)
# Problem 2
# Write a function that returns "penguin" and print the result.
def pen_return():
    return "penguin"
pen = pen_return()
print(pen)
# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.
fruit = ("mango")
print (fruit)
def modify_fruit():
    global fruit
    fruit = "watermelon"
modify_fruit()
print(fruit)
# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.
def combine_string(first_name, last_name):
    return first_name + " " + last_name
print(combine_string("Hamza", "Ramadan"))
# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).
def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)

    return perimeter

print("the perimeter of a 6x3 is:", calculate_perimeter(6, 3))