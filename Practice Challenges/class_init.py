# create a class and object with a specific method

# create class
class Movie:
    def __init__(self, name, studio): # use __init__ to assign values
        self.name = name
        self.studio = studio

    def Watch(self): # create method within class
        msg = "I love to watch {} with my babies!".format(self.name)
        return msg

M1 = Movie("Toy Story", "Pixar") # create object

class Cartoon(Movie): # create child class that inherits parent method 
    pass # Not adding more attributes at this time

M2 = Cartoon("Moana", "Disney") # Create cartoon object

print(M1.name)
print(M1.studio)
print(M1.Watch())

print(M2.Watch()) # used method from parent class Movie on object created with child class Cartoon


    
