# You are tasked with implementing a class hierarchy for a zoo simulation. The zoo has various types of animals, and each animal type has specific properties and behaviors. Use inheritance to create a class hierarchy for the following animal types:

# Mammals
# Mammals have a name and can make a sound.
# Implement a method make_sound() that prints the sound the mammal makes.
# Birds
# Birds have a name and can fly.
# Implement a method fly() that prints a message indicating that the bird is flying.
# Fish
# Fish have a name and can swim.
# Implement a method swim() that prints a message indicating that the fish is swimming.
# Now, create specific animal classes that inherit from these base classes:

# Create a Lion class that inherits from Mammals. Lions make a "Roar" sound.
# Create an Eagle class that inherits from Birds. Eagles can fly at a high altitude.
# Create a Shark class that inherits from Fish. Sharks are excellent swimmers.
# Finally, create instances of each of these animal classes and demonstrate their properties and behaviors.

class Mammal:
    def __init__(self,name):
        self.name = name

    def makeSound(self):
        print("Running for the mammal who didn't provide the makeSound Function")

class Lion(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def makeSound(self):
        print(self.name, " makes Roar sound")

class Deer(Mammal):
    def __init__(self, name):
        super().__init__(name)
    

deerObj = Deer("Deer")

deerObj.makeSound()