divisor = int(input("Ingrese el numero que quiera saber los multiplos:"))

for i in range(1, 12):
    if i % divisor == 0:
        print(i)