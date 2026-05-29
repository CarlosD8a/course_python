# 🏰 Miniproyecto — Ficha de Personaje RPG
# Misión final del módulo:
# Crea un programa que:

# Le pregunte al usuario su nombre, clase y años de experiencia
# Calcule automáticamente: vida máxima (50 + experiencia * 10), maná (30 + experiencia * 5), ataque (10 + experiencia * 3)
# Imprima una ficha de personaje formateada con todos los datos, incluyendo si es "veterano" (más de 5 años de experiencia —
# eso es un booleano)

# Pista de arquitectura: Necesitas input() para recibir datos, conversión de tipos para los números, operadores aritméticos para
# las fórmulas, y f-strings para la ficha final.
# Pista adicional: La línea de es_veterano es una sola línea — una comparación directa guardada en variable.

print("BIENVENIDO AVENTURERO")
print("Es un honor que deses aventurarte en nuestro gremio. Dime cual es tu nombre")
nombre = input("Ingresa tu nombre: ")
print(f"{nombre} mmmm.... Se nota que no eres de por aqui")
print("Dime cual es tu clase?")
clase = input("Ingresa tu clase: ")
print(f"Excelente.... nos hacia falta un gerrero de clase {clase}")
print("Y dime cuantos años tienes en este trabajo??")
xp = int(input("Ingresa tus años de experiencia: "))
print(f"woow.... {xp} eso es increible nos sera de utilidad")
print(f"En hora bueno te has registrado a nuestro gremio guerrero {nombre}")
print("A continuacion estas son tus estadisticas de personaje:")
vida_maxima = 50 + xp * 10
mana = 30 + xp * 5
ataque = 10 + xp * 3
es_veterano = xp > 5
print(
    f"╔══ Hoja de Personaje ══╗\n"
    f"  Nombre      : {nombre}\n"
    f"  Clase       : {clase}\n"
    f"  Vida        : {vida_maxima}\n"
    f"  Ataque      : {ataque}\n"
    f"  Maná        : {mana}\n"
    f"  Es veterano : {es_veterano}\n"
    f"╚═══════════════════════╝"
)
