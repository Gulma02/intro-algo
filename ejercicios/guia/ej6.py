def calcular_porcentajes():
    valor_primer_inversor = int(input("Valor aportado por primer inversor: "))
    valor_segundo_inversor = int(input("Valor aportado por segundo inversor: "))
    valor_tercer_inversor = int(input("Valor aportado por tercer: "))
    total = valor_primer_inversor + valor_segundo_inversor + valor_tercer_inversor

    print("Porcentaje primer inversor: ", valor_primer_inversor*100/total)
    print("Porcentaje segundo inversor: ", valor_segundo_inversor * 100 / total)
    print("Porcentaje tercer inversor: ", valor_tercer_inversor * 100 / total)

calcular_porcentajes()