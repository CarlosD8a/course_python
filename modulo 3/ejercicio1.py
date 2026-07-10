def tocar_nota(nota, duracion=1):
    msg = f"{nota} sonando por {duracion}s"
    return msg


print(tocar_nota("Do", 5))
print(tocar_nota("RE", 2))
print(tocar_nota("MI", 3))
print(tocar_nota("FA", 1))
print(tocar_nota("SO"))
