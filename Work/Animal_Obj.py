from Animals_ABC import Animals


class Animal_Obj(Animals):
    
    def __init__(self, name):
        self.__name = name
        self.__comands = []
        
    def get_name(self):
        return self.__name

    def get_comands(self):
        return self.__comands
    
    def print_name(self):
        print("Имя  -", self.__name)

    def add_animal_skill(self, skill):
        self.__comands.append(skill)
        
    def dell_animal_skill(self, skill):
        self.__comands.remove(skill)
    
    def print_animal_skills(self):
        print(self.__name, "имеет навыки", self.__comands)
        
    def print_count_animal(self,Count):
        self.__Count = Count
        print("Количество животных данного вида = ", self.__Count)
        