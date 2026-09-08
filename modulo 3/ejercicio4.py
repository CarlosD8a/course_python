## funcion creacion de personajej usando kwargs
def new_caracter(name, **specs):
    return f"{name}"


caracter = new_caracter("Terry")
print(caracter)
