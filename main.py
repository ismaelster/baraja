import baraja

baraja_ordenada = baraja.creaBaraja()
print ("Esta es la primera baraja", baraja_ordenada)

baraja_barajada = baraja.creaBaraja()
print ("Esta es la segunda baraja recien creada", baraja_barajada)
baraja.barajar(baraja_barajada)

print ("y ahora la he barajado", baraja_barajada)
