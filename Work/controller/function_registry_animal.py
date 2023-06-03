from Work.model.registry_animal import Registry_animal
from Work.model.animal import Animal


# Класс управляющий регистром животных
class Function_registry_animal:

    def __init__(self, registry_animal: Registry_animal):
        self.registry_animal = registry_animal
# количество животных данного вида    
    def count_domestic_animals(self):
        print("Количество животных данного типа -", self.registry_animal.get_count_domestic_animals())
                
    def count_pack_animals(self):
        print("Количество животных данного типа -", self.registry_animal.get_count_pack_animals())
# список животных
    def list_pack_animal(self):
        for animal in self.registry_animal.get_pack_animal():
            print("Имя -", Animal.get_name_animal(),"   ", "Умения -", Animal.get_skills_animal())
    
    def list_domestic_animal(self):
        for animal in self.registry_animal.get_domestic_animal():
            print("Имя -", Animal.get_name_animal(),"   ", "Умения -", Animal.get_skills_animal())
# выбранное животного и его умения 
    def select_pack_animal(self):
        name_animal = input("")
        for animal in self.registry_animal.get_pack_animal():
            if name_animal == Animal.get_name_animal():
                print("имя животного -", Animal.get_name_animal(),"   ", "умения животного -", Animal.get_skills_animal())
                return
        print("такого животного нет! Попробуйте ещё раз..")
                
    def select_domestic_animal(self):
        name_animal = input("")
        for animal in self.registry_animal.get_domestic_animal():
            if name_animal == Animal.get_name_animal():
                print("имя животного -", Animal.get_name_animal(),"   ", "умения животного -", Animal.get_skills_animal())
                return
        print("такого животного нет! Попробуйте ещё раз..")
# добавить умение
    def add_skill(self, animal: Animal):
        skill = input("")
        animal.add_animal_skill(skill)
        
# удалить умение
    def del_sill(self, animal: Animal):
        skill = input("")
        animal.dell_animal_skill(skill)
        
# добавить животное
    def add_animal (self):
        pass
# удалить животное
    def del_animal (self):
        pass