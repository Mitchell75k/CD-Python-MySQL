class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.Pet.play(pet_cat)
        return self
    
    def feed(self):
        self.Pet.eat(pet_cat)
        return self
    
    def bathe(self):
        self.Pet.noise(pet_cat)
        return self
    
    class Pet: # Inherit from Ninja class
        def __init__(self,name,type,tricks):
            self.name = name
            self.type = type
            self.tricks = tricks
            self.health = 100
            self.energy = 100

        def sleep(self):
            self.energy += 25
            return self

        def eat(self):
            self.energy += 5
            self.health += 10
            return self

        def play(self):
            self.health += 5
            self.energy -= 10
            return self #this is a return of the class Pet, which means it returns the instance of the class Pet so that we can chain methods in the Ninja class (i.e. ninja_mitchell.walk().feed().bathe())

        def noise(self):
            print(f"{self.name} says: Meow!")
            return self
        

# Instanciation Test for Ninja and Pet--------------------------------------------------
ninja_mitchell = Ninja("Mitchell", "Esparza", "Tuna", "Cat Food", "Kitty")

pet_cat = Ninja.Pet("Beltran", "Cat", "Roundhouse Kick")

ninja_mitchell.walk().feed().bathe()

print(pet_cat.health)
print(pet_cat.energy)

pet_cat.sleep()
print(pet_cat.energy)