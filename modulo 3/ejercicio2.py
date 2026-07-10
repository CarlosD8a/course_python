def lanzar_hechizo(nombre, poder, elemento="neutral"):
    msg = f"⚡ {nombre} inflige {poder} de daño ({elemento})"
    return msg


print(lanzar_hechizo("Bola de fuego", 40, "Fuego"))
print(lanzar_hechizo(nombre="Rayo", poder=40, elemento="rasho"))
