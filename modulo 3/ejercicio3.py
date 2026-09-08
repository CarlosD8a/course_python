## crear funcion de combo
def combo(name, *ataques):
    combos = ""
    if ataques:
        combos = " -> ".join(ataques)
        return f"{name} ejecuta combo: {combos}"
    return f"{name} no tiene ataques registrados"


resultado = combo("Terry", "Powe haiser", "Power rocket")
print(resultado)
resultado = combo("Date", "Yamato", "Chacos", "Rebelion")
print(resultado)
resultado = combo(
    "Kirby", "Bola de fuego", "Despertar de los mueros", "Espada", "Genkydama"
)
print(resultado)
resultado = combo("Jake")
print(resultado)
