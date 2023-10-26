from operator import attrgetter

class Pet:
    all = []

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, type):
        if type in Pet.PET_TYPES:
            self._pet_type = type
        else:
            raise ValueError('Not a valid pet type!')


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [p for p in Pet.all if p.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError('Must be an instance of Pet!')
        
    def  get_sorted_pets(self):
        return sorted(self.pets(), key=attrgetter('name'))