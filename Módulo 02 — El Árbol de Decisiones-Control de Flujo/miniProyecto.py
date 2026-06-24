# 🏰 Miniproyecto — Motor de Combate Turn-Based
# Objetivo: Unir todo lo del módulo en un sistema coherente.
# Especificaciones (guía, no código):
# El programa debe:

# Pedir el nombre del héroe al inicio
# Tener un héroe y un enemigo, cada uno con HP y ataque definidos
# Simular turnos de combate con while
# En cada turno, mostrar un mini-menú: [1] Atacar  [2] Usar poción  [3] Huir
# Las pociones son limitadas (máx 2), curan 25 HP, no pueden superar el HP máximo
# Si el héroe huye, termina el combate con mensaje de derrota
# Al terminar, mostrar cuántos turnos duró el combate

# Restricciones de diseño que debes respetar:

# No uses funciones todavía (eso es Módulo 3)
# Toda la lógica va en el flujo principal con if/while/for
# El enemigo debe atacar automáticamente después del turno del héroe
import random

heroe = input("Ingresa tu nombre Heroe: ")
#  ajustar variables a que la vida sea un tope
vida_heroe = 100
daño_espada = 10
vida_enemigo = 75
daño_enemigo = 12
posiones_heroe = 2
posiones_enemigo = 1
curacion = 25
turnos = 0
print("\n" + "═" * 40)
print("⚔️        ¡INICIO DE COMBATE!        ⚔️")
print("═" * 40 + "\n")
while True:
    turnos += 1
    # --- INTERFAZ DE ESTADO (STATUS BOARD) ---
    print("╔" + "═" * 38 + "╗")
    print(
        f"║ ❤️  {heroe[:12].ljust(12)} HP: {str(vida_heroe).ljust(3)}/100  🧪 Pociones: {posiones_heroe} ║"
    )
    print(
        f"║ 👹 Enemigo      HP: {str(vida_enemigo).ljust(3)}/75   🧪 Pociones: {posiones_enemigo} ║"
    )
    print("╚" + "═" * 38 + "╝")

    # --- MENÚ DE ACCIONES ---
    print("\n▶️  ¿Qué deseas hacer?")
    print(" ⚔️  [1] Atacar")
    print(" 🧪 [2] Usar poción")
    print(" 🏃 [3] Huir")
    print("-" * 40)
    try:
        opcion = int(input("👉 Seleccione una opción: "))
        print("-" * 40)
    except ValueError:
        print("⚠️  Ingresa solo números del 1 al 3")
        continue

    # --- TURNO DEL HÉROE ---
    # ATAQUE
    if opcion == 1:
        critico = random.randint(1, 20)
        print(f"💥 ¡{heroe} ataca ferozmente con su espada!")
        if critico > 18:
            print("✨ ¡GOLPE CRÍTICO! El impacto resuena con fuerza (+3 daño).")
            vida_enemigo -= daño_espada + 3
        else:
            print(f"⚔️  Le haces {daño_espada} PD de daño al enemigo.")
            vida_enemigo -= daño_espada
        if vida_enemigo <= 0:
            print("\n💀 ¡El enemigo ha caído ensangrentado!")
            print("🏆 ¡GANASTE EL COMBATE! Que los bardos canten tu victoria.")
            break

    # CURACION
    elif opcion == 2:
        if posiones_heroe > 0:
            print(f"Has usado posion +{curacion} PH")
            vida_heroe = min(vida_heroe + curacion, 100)
        else:
            print("❌ ¡No te quedan pociones en el inventario!")

    # SALIR HUYENDO (FIN DEL JUEGO)
    elif opcion == 3:
        print("\n🏃 Te das la vuelta y huyes despavorido...")
        print("👎 ¡HAS PERDIDO! La cobardía no engendra héroes.")
        break
    else:
        print("⚠️  ¡Selecciona una opción válida del menú!")
        print("═" * 40 + "\n")
        continue  # Reinicia el turno para que no ataque el enemigo por un error de input

    # --- TURNO DEL ENEMIGO ---
    print("\n⏳ Turno del enemigo...")
    accio_enemigo = random.randint(1, 2)
    if accio_enemigo == 1:
        print(
            f"👹 El enemigo se abalanza sobre ti y te inflige {daño_enemigo} PD de daño."
        )
        vida_heroe -= daño_enemigo
        if vida_heroe <= 0:
            print("\n💀 Has caído en combate...")
            print("🪦  GAME OVER. Tu aventura termina aquí.")
            break
    else:
        if posiones_enemigo > 0:
            vida_enemigo = min(vida_enemigo + curacion, 75)
            print("🧪 El enemigo murmura un conjuro y bebe una poción. ¡Se ha curado!")
        else:
            print("💨 El enemigo intenta buscar una poción, pero su bolsa está vacía.")

print("\n" + "═" * 40 + "\n")
