from Work.model.abstract_animal import Abstract_animal

# Класс создающий объект животного
class Animal(Abstract_animal):
    
    def __init__(self, name_animal):
        self.__name_animal = name_animal
        self.__skills_animal = []
        
    def get_name_animal(self):
        return self.__name_animal
        
    def get_skills_animal(self):
        return self.__skills_animal
    
    def print_name_animal(self):
        print("Имя животного -", self.__name_animal)

    def add_animal_skill(self, skill):
        self.__skills_animal.append(skill)
        
    def dell_animal_skill(self, skill):
        self.__skills_animal.remove(skill)
    
    def print_animal_skills(self):
        print(self.__name_animal, "имеет навыки", self.__skills_animal)
        
    def print_count_animal(self):
        print("Количество животных данного вида = ", self.print_count_animal)