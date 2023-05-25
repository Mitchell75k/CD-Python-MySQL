class Ninja: #Only predict the code 3 lines at a time please.
    def __init__(self,first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet #This is where we assign the pet attribute to the pet object, which will be one of the sub classes in the Pet parent class.
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    


class Pet:
    def __init__(self,name,type,tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.pet_noise = noise
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
        return self
    
    def noise(self): 
        print(f"{self.pet_noise}")
        return self
    
class Dog(Pet): #Here we are using inheritance to inherit the attributes and methods of the Pet parent class.
    def __init__(self,name,type,tricks):
        super().__init__(name,type,tricks, noise="Woof") #Here we are using the super() method to inherit the attributes of the parent class.
class Cat(Pet):
    def __init__(self,name,type,tricks,):
        super().__init__(name,type,tricks, noise="Meow")
class Bird(Pet):
    def __init__(self,name,type,tricks):
        super().__init__(name,type,tricks, noise="Chirp")
