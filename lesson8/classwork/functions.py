print("my name is")# print is a function that has string parameter 

def make_greeting(): # define the function
    greeting = "Hello World!"
    return greeting

message = make_greeting() # call the function
print(message)

# function that builds a face
def build_face():
    return ":)"
face = build_face() # call the function
print(face)

def print_poem():
    print("If I were a king,")
    print("I could do anything.")

print_poem()
print_poem()

def perenalized_greeting(name):
    return "hello, " + name + "!"
perenalized_message = perenalized_greeting("Elliot")
print(perenalized_message)
def rectangle_area (length, width):
    area = length * width
    return area

print("the area of a 5x5 is:", rectangle_area(5, 3))