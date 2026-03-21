import random

# Problem 1
# Create a list of 3 operating systems.
# Then reverse the list and print it.
operating_system = ["windows", "linux", "android"]
operating_system.reverse()
print(operating_system)
# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
s = ["math", "science", "reading", "P.E." ]
print(s[1])
sorted_s = sorted(s)  # alphabeticly order
print(sorted_s)
# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
n = ["101", "403", "100", "200", "203"]
print(n)
n.index("403")
print(n.index("403"))
# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
l = ["python","ruby"]
import random
num = random.randint(0, 1)# select random between 0 and 1 inclusive
print(l[num])
l.append("java")
print(l)
# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
password = ["1236","9073","5930","2941","9372","549301"]
len(password)//2
password[len(password)//2]
print(password[len(password)//2])
password.pop(0)
print(password)