class Pet():
    name = None
    fullness = 0 

    def _init_ (self, name):
        self.name = name 

    def eat(self, food):
        print(self.name + " is eating " + food + "...")
        if food == "banana":
            self.fullness = self.fullness + 10
        elif food == "coconut":
            self.fullness = self.fullness + 5
        elif food == "grass":
            self.fullness = self.fullness + 2
        print(self.name + " is now " +self.fullness + "% full")

# Start of program 

pet_owner_name = input("What is your name? ")
print("Welcome ", pet_owner_name)

pet_1 = Pet("Thusan")
pet_1.eat("banana")

