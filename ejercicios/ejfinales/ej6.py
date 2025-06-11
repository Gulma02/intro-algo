import random

n = int(input("Ingresa un numero: "))
suma = 0
secuencia_final = []
last_secuence = []
grouped_secuences = []

for i in range(n):
    numero = random.randint(1, 20)
    if numero + suma <= 20:
        last_secuence.append(numero)
        secuencia_final.append(numero)
        suma += numero
    else:
        grouped_secuences.append(last_secuence)
        last_secuence = [numero]
        secuencia_final.append(0)
        suma = numero
        secuencia_final.append(numero)

    if i == n:
        grouped_secuences.append(last_secuence)

print("Esta es la secuencia final: ", secuencia_final)
print("Estos son los grupos: ", grouped_secuences)
longest_secuence_length = 0
longest_secuences = []

for grouped_secuence in grouped_secuences:
    if len(grouped_secuence) > longest_secuence_length:
        longest_secuence_length = len(grouped_secuence)
        longest_secuences = [grouped_secuence]
    elif len(grouped_secuence) == longest_secuence_length:
        longest_secuences.append(grouped_secuence)

print(longest_secuences)
