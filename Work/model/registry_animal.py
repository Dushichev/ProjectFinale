from Work.model.animal import Animal

class Registry_animal:
    
    def __init__(self):
        self.__pack_animal = []
        self.__domestic_animal = []
        self.__count_pack_animals = 0
        self.__count_domestic_animals = 0
        
    def get_pack_animal(self):
        return self.__pack_animal
    
    def get_domestic_animal(self):
        return self.__domestic_animal
    
    def get_count_pack_animals(self):
        return self.__count_pack_animals
    
    def get_count_domestic_animals(self):
        return self.__count_domestic_animals
    
        
    def add_pack_animal(self, new_animal: Animal):
        self.__pack_animal.append(new_animal)
        self.__count_pack_animals += 1
    
    def add_domestic_animal(self, new_animal: Animal):
        self.__domestic_animal.append(new_animal)
        self.__count_domestic_animals +=1