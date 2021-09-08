# In the notes we saw the PetFactory abstract class and the DogFactory.
# Implment a CatFactory below.


from abc import ABC, abstractmethod

class Animal(ABC):
    pass

class PetFood(ABC):
    pass

class PetToy(ABC):
    pass    

class PetFactory(ABC):
    @abstractmethod
    def get_animal(self):
        pass

    @abstractmethod
    def get_pet_food(self):
        pass

    @abstractmethod
    def get_pet_toy(self):
        pass


