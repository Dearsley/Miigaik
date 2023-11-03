from Paradox.monty_hall import *
from Paradox.birthday import *


def show():
    monty_hall_iteration = input("Введите количество итераций: ")
    birthday_group = input("Введите количество человек в группе: ")
    birthday_iteration = input("Введите количество итераций: ")

    print(f"Monty Hall: {monty_hall(int(monty_hall_iteration))} %" if monty_hall_iteration.isdigit() else f"Monty Hall: {monty_hall()} %")

    if birthday_iteration.isdigit():
        print(f"Birthday: {birthday(iterations=int(birthday_iteration))} %")
    elif birthday_group.isdigit():
        print(f"Birthday: {birthday(people_in_group=int(birthday_group))} %")
    elif birthday_iteration.isdigit() and birthday_group.isdigit():
        print(f"Birthday: {birthday(int(birthday_group), int(birthday_iteration))} %")
    else:
        print(f"Birthday: {birthday()} %")

    if __name__ == "__main__":
        show()
