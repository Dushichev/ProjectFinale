from Add_animals import Add_animals
from Animal_Obj import Animal_Obj

class Registry_animals:

    def __init__(self, Add_animals: Add_animals):
        self.Add_animals = Add_animals
  
    def count_domestic_animals(self):
        print("Количество животных данного типа -", self.Add_animals.get_count_domestic_animals())
                
    def count_pack_animals(self):
        print("Количество животных данного типа -", self.Add_animals.get_count_pack_animals())

    def list_pack_animal(self):
        for animal in self.Add_animals.get_pack_animal():
            print("Имя -", Animal_Obj.get_name(),"   ", "Умения -", Animal_Obj.get_comands())
    
    def list_domestic_animal(self):
        for animal in self.Add_animals.get_domestic_animal():
            print("Имя -", Animal_Obj.get_name(),"   ", "Умения -", Animal_Obj.get_comands())

    def select_pack_animal(self):
        name_animal = input("")
        for name_animal in self.Add_animals.get_pack_animal():
            if name_animal == Animal_Obj.get_name():
                print("имя животного -", Animal_Obj.get_name(),"   ", "умения животного -", Animal_Obj.get_command())
                return
        print("такого животного нет! Попробуйте ещё раз..")
                
    def select_domestic_animal(self):
        name_animal = input("")
        for animal in self.Add_animals.get_domestic_animal():
            if name_animal == Animal_Obj.get_name():
                print("имя животного -", Animal_Obj.get_name(),"   ", "умения животного -", Animal_Obj.get_command())
                return
        print("такого животного нет! Попробуйте ещё раз..")

    def add_skill(self, animal: Animal_Obj):
        skill = input("")
        animal.add_animal_skill(skill)
        

    def del_sill(self, animal: Animal_Obj):
        skill = input("")
        animal.dell_animal_skill(skill)
        

    def add_animal (self):
        pass

    def del_animal (self):
        pass