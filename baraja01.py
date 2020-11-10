palos = ["o", "c", "e", "b"]
numeros = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]


# funcion para crear baraja
def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja
