class dog:
    print("Hi, I am a dog profile class!")

dog_object = dog()
class DogProfile:
    category="dog"
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age=age
        self.favourite_food = favourite_food

dog1 = DogProfile("Ice", "Golden Retirever", 6, "Cookies")
dog2 = DogProfile("Hunt", "Poodle", 14, "Fish")

print("{} is a {} and is {} years old.".format(dog1.name, dog1.animal_type, dog1.age))
print("{}likes eating {}.".format(dog1.name, dog1.favourite_food))

print("{} is a {} and is {} years old.".format(dog2.name, dog2.animal_type, dog2.age))
print("{}likes eating {}.".format(dog2.name, dog2.favourite_food))
