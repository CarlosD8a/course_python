# Reto 2.1 — Sistema de turnos básico
# Crea un simulador de combate por turnos. El héroe tiene 100 HP, el enemigo 60 HP. Cada turno, el héroe hace 15 de daño y
# el enemigo hace 10. Usa while para que el combate continúe hasta que alguno llegue a 0 HP.
# Imprime el estado de HP en cada turno e indica quién ganó.


heroe = 100
daño_hereo = 15
enemigo = 60
daño_enemigo = 10

print("Inicia el combate")
while heroe > 0 and enemigo > 0:
    enemigo -= daño_hereo
    heroe -= daño_enemigo
    enemigo = max(enemigo, 0)
    heroe = max(heroe, 0)
    print("Estatus:")
    print(f"Heroe: {heroe}")
    print(f"Enemigo: {enemigo}")

print("El ganador es")
if heroe > 0:
    print("El Heroe")
else:
    print("El enemgigo")
