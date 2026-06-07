# Reto 2.2 — Dungeon con trampas
# Tienes una lista de 8 habitaciones: algunas son "segura", otras son "trampa".
# Recorre el dungeon con for. Si la habitación es trampa, imprime una advertencia y usa continue para no recoger el botín.
# Si encuentras la habitación "jefe", imprime "¡Combate final!" y detén la exploración con break.

rooms = ["segura,segura", "trampa", "segura", "trampa", "segura", "segura", "jefe"]

for room in rooms:
    if room == "trampa":
        print(
            "Advetencia, hay demasiados enemigos en esta habitacion continua sin provocarlos"
        )
        continue
    elif room == "jefe":
        print("combate final")
        break
    else:
        print("La habitacion parece segura, es momento de recoger el loot")
