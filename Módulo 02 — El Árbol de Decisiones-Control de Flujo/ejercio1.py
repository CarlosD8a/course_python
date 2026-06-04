# Reto 1.1 — La puerta del dungeon
# Pide al usuario su nivel de personaje. Si es mayor o igual a 5, imprímelo "Puedes entrar al dungeon".
# Si es entre 1 y 4, "Necesitas más experiencia". Si es 0 o menos, "Eso no es un nivel válido, aventurero".

print("Bienvenido a la dangeon viajero")
nivel = int(input("Ingrese su nivel por favor: "))
if nivel >= 5:
    print("Bienvenido puedes pasar")
elif 1 <= nivel <= 4:
    print("Lo siento viajero, necesitas mas experiencia")
else:
    print("Eso no es un nivel valido, aventurero")
