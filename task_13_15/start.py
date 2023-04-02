import bd_Animals

import sys

print(f"Добро пожаловать!")


def main():
    print(f"\n"
          f"Введите команду для действия! \n"
          f"Либо введите info")
    st = (input("Ввод: ").lower())
    if st == "info":
        print(f"show_t - показать весь список животных. \n"
              f"show - показать таблицу с одним типом животных. \n" 
              f"add - добавить животное в список. \n"
              f"comm - добавить команду для животного. \n"
              f"sh_comm - вывести команды животного. \n"
              f"return - возрат. \n"
              f"exit - выход. \n")
    elif st == "show_t":
        bd_Animals.show_tables()
    elif st == "show":
        bd_Animals.show()
    elif st == "add":
        bd_Animals.add_animal()
    elif st == "comm":
        bd_Animals.add_command()
    elif st == "sh_comm":
        bd_Animals.sh_command()
    elif st == "return":
        return main()
    elif st == "exit":
        return sys.exit()
    else:
        return main()
    return main()


main()
