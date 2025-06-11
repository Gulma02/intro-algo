def convertir_medida():
    medida_en_metros: float = float(input("Altura en metros: "))
    medida_en_centimetros: int = int(medida_en_metros*100)
    print("Su medida en centimetros: ", medida_en_centimetros)
    medida_en_pulgadas: float = float(medida_en_centimetros/0.39)
    print("Su medida en pulgadas: ", medida_en_pulgadas)
    medida_en_pies: float = float(medida_en_pulgadas/12)
    print("Su medida en pies: ", medida_en_pies)
    medida_en_yardas: float = float(medida_en_pies/365)