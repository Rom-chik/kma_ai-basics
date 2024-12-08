import random
import time


def petri_net_simulation():
    print("Історія починається!")
    time.sleep(1.5)
    print("Студент вирішує купити авто.")
    time.sleep(1)

    # Початкові умови
    G = random.choice([0, 1])
    print(f" G = {G}")
    time.sleep(1)
    print("Студент рахує свої накопичення... ")
    time.sleep(2)
    Y = 1  # Гроші
    print("5000$ = 1 Y")
    time.sleep(2)

    # Вибір авто
    print("Студент вибирає авто.")
    time.sleep(2)
    choice = random.choice(["speed", "comfort"])

    if choice == "speed":
        R = 1
        B = 0
        print("Він надає перевагу швидкості")
    else:
        R = 0
        B = 1
        print("Він надає перевагу комфорту")
    print(f"{'R = 1' if choice == 'speed' else 'B = 1'}")
    time.sleep(2)

    # Зважає на цінову категорію
    if choice == "speed":
        if G == 1:
            print("Цей студент точно вміє заробляти гроші")
            time.sleep(2)
            print("Влаштовується на гарну роботу")
            time.sleep(1)
            Y += 7
            print("І заробляє велику суму... 30000$")
            print("Y = 1 + 7")
            time.sleep(1.5)
        else:
            print("На жаль, цей студент не вміє заробляти гроші")
            time.sleep(2)
            print("Підрацьовує лише на канікулах")
            time.sleep(1)
            Y += 1
            print("Але заробляє достатню суму грошей.. 5000$")
            print("Y = 1 + 1")
            time.sleep(1.5)
    else:  # comfort
        if G == 1:
            print("Цей студент точно вміє заробляти гроші")
            time.sleep(2)
            print("Влаштовується на гарну роботу")
            time.sleep(1)
            Y += 5
            print("І заробляє непогану суму... 25000$")
            print("Y = 1 + 5")
            time.sleep(1.5)
        else:
            print("На жаль, цей студент не вміє заробляти гроші")
            time.sleep(2)
            print("Відпочиває на канікулах")
            time.sleep(1)
            Y = 0
            print("І витрачає всі накопичення(")
            print("Y = 0")
            time.sleep(1.5)

    # Перевіряє ринок автомобілів
    print("Студент перевіряє ринок автомобілів")
    time.sleep(1.5)
    if Y >= 7 and R == 1:
        print("Обирає Infiniti Q60 2021")
        time.sleep(1.5)
        print("Стає щасливим власником автомобіля!")
    elif Y >= 2 and R == 1:
        print("Обирає Subaru Impreza 2006")
        time.sleep(1.5)
        print("Стає щасливим власником автомобіля!")
    elif Y >= 6 and B == 1:
        print("Обирає Mercedes-Benz GLE 2016")
        time.sleep(1.5)
        print("Стає щасливим власником автомобіля!")
    else:
        print(", йому ні нащо не вистачає(")
        print("Тому Купує річний проїзний на метро.")
        time.sleep(1.7)
        print("І вимушений ходити пішки далі..")
    time.sleep(1.5)
    print("Історія завершилась!")


# Запуск симуляції
petri_net_simulation()
