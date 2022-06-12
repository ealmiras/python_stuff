class Cat:
    def __init__(self, name):
        self.name = name
        # print("INSIDE CAT INIT")
    
    def meow(self):
        print(f"{self.name} meows")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs")

class Lion(Cat):
    def __init__ (self, name, pride_name):
        # print("INSIDE LION INIT")
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars")

cat1 = Cat("Leyla")
lion1 = Lion("Blue", "XYZ")
puma1 = Cougar("Elton")

# cat1.meow()

# lion1.meow()
# lion1.roar()

# puma1.meow()
# puma1.purr()

