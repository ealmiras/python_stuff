class Dog:
    species = "canine"
    num_dogs = 0

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1
    
    @classmethod
    def register_stray(cls):
        return cls("coming soon", "unknown", "unkown")
    
    def learn_trick(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
        print(f"Tricks {self.name} knows are:")
        print(self.tricks)
    
    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} doesn't know how to {trick}!")
    
    def bark(self):
        print(f"{self.name} says WOOF!")
    

# print(Dog.num_dogs)

elton = Dog("Elton", "Pug", 97236)
# elton.learn_trick("sit")
# elton.perform_trick("sit")
# elton.perform_trick("spin")
# elton.bark()

# print(elton.species)
# print(Dog.species)

Dog.species = "C. Lupus"
# print(Dog.species)
# print(elton.species)

# print(Dog.num_dogs)
