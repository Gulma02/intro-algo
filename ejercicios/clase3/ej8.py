import random

values = [int(random.randint(1, 6)), int(random.randint(1, 6)), int(random.randint(1, 6))]
count = 0
for value in values:
    if value == 6:
        count += 1

match count:
    case 1:
        print("Regular")
    case 2:
        print("Muy bien!")
    case 3:
        print("Excelente!")
    case 0:
        print("Pesimo")