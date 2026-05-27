# 🟡 Ejercicio 2 — Nivel: Caballero
# Misión: Simula un sistema de daño básico. Tienes:

vida_enemigo = 250
ataque_base = 45
multiplicador_critico = 1.8

# Calcula:

# El daño de un golpe normal
# El daño de un golpe crítico
# La vida restante del enemigo tras ambos golpes
# Si el enemigo sigue vivo (usa un booleano)

# Pista: El multiplicador trabaja con *. El resultado de si sigue vivo es una comparación — ¿cuál operador usarías?

danio_normal = ataque_base
danio_critico = ataque_base * multiplicador_critico
vida_restante = vida_enemigo - danio_normal - danio_critico
enemigo_vivo = vida_restante > 0  # True o False directo

print(f"Golpe normal  : {danio_normal}")
print(f"Golpe crítico : {danio_critico}")
print(f"Vida restante : {vida_restante}")
print(f"¿Sigue vivo?  : {enemigo_vivo}")
