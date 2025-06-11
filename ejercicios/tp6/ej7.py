def mcd(a, b):
    if a > b:
        minimo = b
    else:
        minimo = a

    maximo_comun_divisor = 0
    for num in range(1, minimo):
        if a % num == 0 and b % num == 0:
            maximo_comun_divisor = num

    return maximo_comun_divisor

print(mcd(30, 40))