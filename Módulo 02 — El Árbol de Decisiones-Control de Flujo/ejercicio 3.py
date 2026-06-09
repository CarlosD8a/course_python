# 🔴 Nivel 3 — Jefe final del módulo
# Reto 3.1 — El Oráculo de Decisiones
# Crea un menú interactivo con while True que le pregunte al usuario qué quiere hacer:
# 1. Ver estadísticas
# 2. Atacar
# 3. Usar poción
# 4. Huir (salir del programa)
# Cada opción debe tener una respuesta distinta. Si elige una opción inválida, muestra un error y vuelve a preguntar.
# Solo el 4 debe terminar el loop.
print("BIENVENIDO")
print("Menu principal")
posiones = 3
vida = 100
while True:
    print(
        "==========Opciones==========\n"
        "1. Ver estadísticas\n"
        "2. Atacar\n"
        "3. Usar poción\n"
        "4. Huir (salir del programa)\n"
        "============================"
    )
    try:
        opcion = int(input("Selecciones una opcion del menu: "))
        if opcion == 1:
            print(f"""                  
=================================
Seleccionaste la opcion: {opcion}
================================
""")
            print(f"""
=======Estadisticas=======
Nombre:...........Parzival
Clase:............Guerrero
Arma:...............Espada
Posiones:................{posiones}
vida:................{vida}
Experiencia:..........20xp
==========================
""")
        elif opcion == 2:
            print(f"""                  
=================================
Seleccionaste la opcion: {opcion}
================================
""")
            print("Has atacado al enemigo")
        elif opcion == 3:
            print(f"""                  
=================================
Seleccionaste la opcion: {opcion}
================================
""")
            if posiones > 0:
                print("Has usado posion de curacion, vida aumenta +10ph")
                vida += 10
                posiones -= 1
            else:
                print("Ya no te quedan posiones por consumir")
        elif opcion == 4:
            print("Has salido corriendo\nTermino el combate")
            break
        else:
            print("Por favor selecciona una opcion de la lista")
    except ValueError:
        print("Algo ocurrio mal")
