import os
from colorama import Fore, Style


def menu():
    while True:
        print(Fore.LIGHTCYAN_EX,
              "\n\t|-------Menu-------|",
              Fore.LIGHTGREEN_EX,
              "\n\t1. Lab - 1 (Побудова мінімального остового дерева - Алгоритм Крускала)"
              "\n\t2. Lab - 2 (Задача листоноші)"
              "\n\t3. Lab - 3 (Задача комівояжера)"
              "\n\t4. Lab - 4 (Потокові алгоритми)"
              "\n\t5. Lab - 5 (Ізоморфізм графів)",
              Fore.LIGHTRED_EX,
              "\n\t0. Exit")
        try:
            choice = int(input(f"{Fore.LIGHTMAGENTA_EX}Виберіть елемент меню: "))
            match choice:
                case 1:
                    print("Lab_1\n")
                    os.system('python3 1_Lab/1_lab.py')  # замініть 'my_script.py' на свій файл
                    continue
                case 2:
                    print("Lab_2\n")
                    os.system('python3 2_Lab/2_lab.py')  # замініть 'my_script.py' на свій файл
                    continue
                case 3:
                    print("Lab_3\n")
                    os.system('python3 3_Lab/3_lab.py')  # замініть 'my_script.py' на свій файл
                    continue
                case 4:
                    print("Lab_4\n")
                    os.system('python3 4_Lab/4_lab.py')  # замініть 'my_script.py' на свій файл
                    continue
                case 5:
                    print("Lab_5\n")
                    os.system('python3 5_Lab/5_lab.py')  # замініть 'my_script.py' на свій файл
                    continue
                case 0:
                    print("Exit")
                    break
                case _:
                    print(f"\n{Fore.LIGHTRED_EX}Такого елементу меню не існує{Style.RESET_ALL}")
        except ValueError:
            print(f"\n{Fore.LIGHTRED_EX}Ви ввели не цифрове значення{Style.RESET_ALL}")





if __name__ == '__main__':
    menu()
    # os.startfile("1_Lab/1_lab.py") # <-- не потрібно
