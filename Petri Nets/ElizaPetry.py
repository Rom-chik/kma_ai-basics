import time
import random

# Симуляція історії
print("Історія починається!")
time.sleep(1)
print("Сесія розпочалась.")
time.sleep(1)

# Задається натхнення студента
inspiration = random.choice([2, 3])
#inspiration = 3
print(f"і в цей момент студент має натхнення: {inspiration}")
time.sleep(1.5)
print("Екзамен через тиждень...")
time.sleep(1.2)

# Початкова ситуація
student_decision = "Студент вирішує що робити"
print("Студент вирішує що робити")
time.sleep(1.2)


print("Обирає пограти в нового Сталкера")
time.sleep(1.5)
if inspiration > 1:
    print("також випити вина")
    time.sleep(1.5)
if inspiration > 2:
    print("Ну і почати готуватись до екзамену")
    time.sleep(1.5)


# Переходи без вибору
print("Студент вирішує Пройти сюжетну лінію.")
time.sleep(1.5)
if inspiration > 1:
    print("Також вирішує Обговорити римську імперію.")
    time.sleep(1.5)

if inspiration > 2:
    print("Не забуває й попросити конспекти для підготовки.")
    time.sleep(1.5)
    print("Випадково знаходить варіанти минулих років.")
    time.sleep(1.5)
    print("Кладе книжку під подушку в надії здати екзамен.")
    time.sleep(1.5)

# Рішення між 'Байдикувати далі' і 'Перестати байдикувати'
print("Але вимушений зробити складний вибір...")
time.sleep(2)
print("Викластись на повну, чи грати й пити.")
time.sleep(2)
if random.choice([True, False]):
    print("Студент вирішує Байдикувати далі.")
    time.sleep(1.7)
    print("І завалює сесію..")
    time.sleep(1)
else:
    print("Бере себе в руки і обирає Перестати байдикувати!")
    time.sleep(1.7)
    print("Виділяє себе всього на підготовку")
    time.sleep(1.7)
    print("І складає сесію!  =)")
    time.sleep(1)

print("Історія завершилась!")
