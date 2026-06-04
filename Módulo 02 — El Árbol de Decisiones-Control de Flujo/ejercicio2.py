# Reto 1.2 — Inventario de ítems
# Tienes esta lista: ["espada", "poción", "escudo", "antorcha", "llave"]. Usa un for para imprimir cada ítem numerado
# (1. espada, 2. poción...).
# Pista: existe una función que te da índice y valor al mismo tiempo.

inventario = ["espada", "poción", "escudo", "antorcha", "llave"]
for indice, item in enumerate(inventario):
    print(f"{indice + 1}. {item}")
