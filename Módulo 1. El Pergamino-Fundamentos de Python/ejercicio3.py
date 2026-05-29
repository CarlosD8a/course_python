# 🔴 Ejercicio 3 — Nivel: Paladín
# Misión: El sistema de turnos de batalla.
# Un combate tiene turnos. La velocidad del héroe determina cada cuántos turnos del enemigo actúa el héroe.

velocidad_heroe = 7
velocidad_enemigo = 3

# Sin usar if ni ciclos (aún no los vemos), calcula solo con operadores:

# ¿En el turno 21, actúa el héroe? ¿Y el enemigo? (Pista: módulo)
accion_hero = 21 % velocidad_heroe == 0
accion_enemigo = 21 % velocidad_enemigo == 0
print(f"Turno 21 - Heroe actua:{accion_hero}")
print(f"Turno 21 - Enemigo actua:{accion_enemigo}")
# ¿Cuántos turnos completos de héroe caben en 100 turnos totales?
turnos_completos_heroe = int(100 / velocidad_heroe)
turnos_completos_enemigo = int(100 / velocidad_enemigo)
print(f"El heroe da: {turnos_completos_heroe} turnos")
print(f"El enemigo da: {turnos_completos_enemigo} turnos")
# Imprime un mensaje que diga: "Turno 21 — Héroe actúa: [True/False] | Enemigo actúa: [True/False]" usando f-strings

# Pista: Si 21 % 7 == 0 el héroe actúa. Una comparación devuelve True o False directamente — puedes guardar eso en una variable.
