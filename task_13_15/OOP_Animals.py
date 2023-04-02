# Животные имена команды кличи
class Animals:
    def __init__(self, name, command, birthday):
        self.name = name
        self.command = command
        self.birthday = birthday


# вьючные или домашние
# class AnimalsClass(Animals):
#     def __init__(self, cl_animals, name, command, birthday):
#         super().__init__(name, command, birthday)
#         self.cls_animals = cl_animals


# кошки, собаки и т.п.
class TypeAnimals(Animals):
    def __init__(self, name, command, birthday, type_animals):
        super().__init__(name, command, birthday)
        self.cls_animals = None
        self.type_animals = type_animals

    def write_animals(self):
        if self.type_animals in ("cat", "dog", "hamster"):
            self.cls_animals = "home animals"
            return f"{self.name}, {self.command}, {self.birthday}, {self.cls_animals}, {self.type_animals}"
        elif self.type_animals in ("horse", "donkey", "camel"):
            self.cls_animals = "pack animals"
            return f"{self.name}, {self.command}, {self.birthday}, {self.cls_animals},  {self.type_animals}"
        elif self.type_animals != ("cat", "dog", "hamster", "horse", "donkey", "camel"):
            print("Вы ввели не правильный тип животных")
            self.type_animals = input("Input type animal: ")
            return f"{self.name}, {self.command}, {self.birthday}, {self.cls_animals},  {self.type_animals}"


# метод запуска
def xyz():
    add_animals = TypeAnimals(input("Input name: "), input("Input command: "), input("Inpt birthday: "),
                              input("Input type animal: "))
    return add_animals.write_animals()
