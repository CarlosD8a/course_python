# 🟢 Ejercicio 1 — Nivel: Escudero
# Misión: Crea variables para describir a tu personaje: nombre, clase (guerrero/mago/arquero), nivel, vida, maná y si está vivo o no.
# Luego imprímelas todas en un solo print usando f-strings con un formato bonito tipo ficha de RPG.
# Pista: Piensa en qué tipo de dato corresponde a cada atributo. ¿El nivel es entero o decimal? ¿El nombre es número?

nombre = "Parzival"
clase = "Guerrero/Forastero"
nivel = 1
vida = 80
mana = 10.0
vivo = True

# Versión más legible (mismo resultado)
print(
    f"╔══ Hoja de Personaje ══╗\n"
    f"  Nombre : {nombre}\n"
    f"  Clase  : {clase}\n"
    f"  Nivel  : {nivel}\n"
    f"  Vida   : {vida}\n"
    f"  Maná   : {mana}\n"
    f"  Vivo   : {vivo}\n"
    f"╚═══════════════════════╝"
)
