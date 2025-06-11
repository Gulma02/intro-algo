def main(a, b):
    num_final = 1
    for num in range(b):
        num_final *= a

    print(num_final)


main(4, 2)