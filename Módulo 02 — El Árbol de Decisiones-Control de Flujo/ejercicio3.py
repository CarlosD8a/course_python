# Reto 1.3 — Cuenta regresiva de stamina
# Usa range() para imprimir la stamina de tu personaje contando desde 10 hasta 1, y al final imprime "¡Sin stamina! Turno terminado.".

estamina = 10
for accion in range(estamina, 0, -1):
    print(accion)
    if accion == 1:
        print("¡Sin stamina! Turno terminado.")
