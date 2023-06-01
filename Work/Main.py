from Registry_animals import Registry_animals

class Main:
    
    def __init__(self, Registry_animals: Registry_animals):
        self.Registry_animals = Registry_animals
    
    def menu(self):
        while(True):
            print("Меню:\nВыберите класс животного")
            print("1. Вьючные")
            print("2. Домашние")
            print("3. выход")
            x = int(input(""))
            if x == 1:
                while(True):
                    print("1. список животных")
                    print("2. Выбрать животное, для просмотра навыков")
                    print("3. Добавить  животное")
                    print("4. Удалить животное")
                    print("5. Посмотреть количество животных данного класса")
                    print("6. Вернутся в предыдущее меню")
                    print("7. выход")
                    x = int(input(""))
                    if x == 1:
                        self.Registry_animals.list_pack_animal()
                    if x == 2:
                        print("Введите имя животного:")
                        self.Registry_animals.select_pack_animal()
                    if x == 3:
                        pass
                    if x == 4:
                        pass
                    if x == 5:
                        self.Registry_animals.count_pack_animals()
                    if x == 6:
                        break
                    if x == 7:
                        return
            elif x == 2:
               while(True):
                    print("1. Посмотреть список животных")
                    print("2. Выбрать животное, для просмотра навыков")
                    print("3. Добавить новое животное")
                    print("4. Удалить животное")
                    print("5. Посмотреть количество животных данного класса")
                    print("6. Вернутся в предыдущее меню")
                    print("7. Exit")
                    x = int(input(""))
                    if x == 1:
                        self.Registry_animals.list_domestic_animal()
                    if x == 2:
                        print("Введите имя животного:")
                        self.Registry_animals.select_domestic_animal()
                    if x == 3:
                        pass
                    if x == 4:
                        pass
                    if x == 5:
                        self.Registry_animals.count_domestic_animals()
                    if x == 6:
                        break
                    if x == 7:
                        return
            elif x == 3:
                return
            else:
                print("попробуйте снова..")


   