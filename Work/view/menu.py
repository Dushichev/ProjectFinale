from Work.controller.function_registry_animal import Function_registry_animal

class Menu:
    
    def __init__(self, func_registry_animals: Function_registry_animal):
        self.func_registry_animals = func_registry_animals
    
    def menu(self):
        while(True):
            print("Меню:\nВыберите класс животного")
            print("1. Pack_animal")
            print("2. Domestic_animal")
            print("3. Exit!")
            x = int(input(""))
            if x == 1:
                while(True):
                    print("1. Посмотреть список животных")
                    print("2. просмотр навыков")
                    print("3. Добавить животное")
                    print("4. Удалить животное")
                    print("5. Посмотреть количество животных")
                    print("6. Вернутся в предыдущее меню")
                    print("7. выход")
                    x = int(input(""))
                    if x == 1:
                        self.func_registry_animals.list_pack_animal()
                    if x == 2:
                        print("Введите имя животного:")
                        self.func_registry_animals.select_pack_animal()
                    if x == 3:
                        pass
                    if x == 4:
                        pass
                    if x == 5:
                        self.func_registry_animals.count_pack_animals()
                    if x == 6:
                        break
                    if x == 7:
                        return
            elif x == 2:
               while(True):
                    print("1. список животных")
                    print("2. просмотр навыков")
                    print("3. Добавить животное")
                    print("4. Удалить животное")
                    print("5. Посмотреть количество животных")
                    print("6. Вернутся в предыдущее меню")
                    print("7. выход")
                    x = int(input(""))
                    if x == 1:
                        self.func_registry_animals.list_domestic_animal()
                    if x == 2:
                        print("Введите имя животного:")
                        self.func_registry_animals.select_domestic_animal()
                    if x == 3:
                        pass
                    if x == 4:
                        pass
                    if x == 5:
                        self.func_registry_animals.count_domestic_animals()
                    if x == 6:
                        break
                    if x == 7:
                        return
            elif x == 3:
                return
            else:
                print("Error")
            