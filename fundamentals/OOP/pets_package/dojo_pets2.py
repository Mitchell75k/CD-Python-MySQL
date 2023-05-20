from dojo_pets_module import Ninja, Pet, Dog, Cat, Bird
#Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
#Have the Ninja feed, walk, and bathe their pet.

ninja_mitchell = Ninja("Mitchell", "Esparza", Dog("Romeo", "Chihuahua", "backflip"), "Bacon", "Purina")
print(ninja_mitchell.first_name, ninja_mitchell.last_name, ninja_mitchell.treats, ninja_mitchell.pet_food)
print(ninja_mitchell.pet.name, ninja_mitchell.pet.type, ninja_mitchell.pet.tricks, ninja_mitchell.pet.pet_noise)
ninja_mitchell.feed().walk().bathe()
print(ninja_mitchell.pet.health, ninja_mitchell.pet.energy)

ninja_ash = Ninja("Ash", "Vasquez", Cat("Beltran", "Black Cat", "Lay on back"), "Sardines", "Purina+")
print(ninja_ash.first_name, ninja_ash.last_name, ninja_ash.treats, ninja_ash.pet_food)
print(ninja_ash.pet.name, ninja_ash.pet.type, ninja_ash.pet.tricks, ninja_ash.pet.pet_noise)
ninja_ash.feed().walk().bathe().feed()
print(ninja_ash.pet.health, ninja_ash.pet.energy)

