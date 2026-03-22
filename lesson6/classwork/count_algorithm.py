numbers = [17,3,67,53,2,5]

counter = 0

for i in range (len(numbers)):
    item = numbers[i]
    if item > 5 :
        counter = counter +1 
print("there are",counter,"numbers greater than 5 in our list.")

l = ["cat", "dog","hamster"]

counter2 = 0

for i in range (len(l)):
    item = l[i]
    if item  == "cat":
        counter2 = counter2 +1
print("There are", counter2, "cats in our list.")

num_cats = l.count("cat")
print("There are", num_cats, "cats in our list.")