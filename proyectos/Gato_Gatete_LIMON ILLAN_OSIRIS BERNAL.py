# [Nombre del juego]: Gato Gatete
# [Nombres de los integrantes]: Sarah Lim0n, Lizbeth Osiris Lizbeth
# [Fecha]: 23/11/2026

import random


def leer_texto(mensaje):
    """Pide un texto y no permite respuestas vacias."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("No dejes la respuesta vacia.")


def leer_numero(mensaje, minimo, maximo):
    """Pide un numero entero dentro de un rango."""
    while True:
        texto = input(mensaje).strip()
        if not texto or not texto.isdigit():
            print("Escribe un numero valido.")
            continue
        numero = int(texto)
        if minimo <= numero <= maximo:
            return numero
        print("Elige un numero entre", minimo, "y", maximo)


def leer_opcion(mensaje, opciones):
    """Pide una opcion y repite hasta recibir una valida."""
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones:
            return opcion
        print("Opcion invalida.")


def elegir_dificultad():
    """Devuelve el nivel elegido por el jugador."""
    print("\nDificultad:")
    print("1. cachorros - facil")
    print("2. gato - medio")
    print("3. gatote - imposible")
    opcion = leer_opcion("Elige 1, 2 o 3: ", ("1", "2", "3"))
    if opcion == "1":
        return "cachorros"
    elif opcion == "2":
        return "gato"
    else:
        return "gatote"


def crear_laberinto(dificultad):
    """Crea la matriz del laberinto segun la dificultad."""
    laberinto = [
        ["G", ".", ".", "#", "."],
        [".", "#", ".", ".", "."],
        [".", ".", "#", "#", "."],
        ["T", ".", ".", "P", "."],
        [".", ".", "#", ".", "S"],
    ]

    if dificultad == "gato" or dificultad == "gatote":
        laberinto[1][3] = "T"
        laberinto[3][2] = "T"
    if dificultad == "gatote":
        laberinto[0][2] = "T"
        laberinto[4][1] = "T"

    return laberinto


def mostrar_laberinto(laberinto, fila_jugador, columna_jugador, inicial):
    """Muestra la matriz con ciclos anidados."""
    print("\nLeyenda:", inicial + "=tu gato,", ".=camino,", "#=pared")
    print("         T=trampa, P=premio, S=salida")
    for fila in range(len(laberinto)):
        linea = ""
        for columna in range(len(laberinto[fila])):
            if fila == fila_jugador and columna == columna_jugador:
                linea += inicial + " "
            else:
                linea += laberinto[fila][columna] + " "
        print(linea)
    print()


def mover_gato(laberinto, fila, columna, direccion):
    """Intenta mover al gato y devuelve la posicion nueva."""
    nueva_fila = fila
    nueva_columna = columna

    if direccion == "w":
        nueva_fila -= 1
    elif direccion == "s":
        nueva_fila += 1
    elif direccion == "a":
        nueva_columna -= 1
    elif direccion == "d":
        nueva_columna += 1

    if nueva_fila < 0 or nueva_fila >= len(laberinto):
        return fila, columna, False
    if nueva_columna < 0 or nueva_columna >= len(laberinto[0]):
        return fila, columna, False
    if laberinto[nueva_fila][nueva_columna] == "#":
        return fila, columna, False
    return nueva_fila, nueva_columna, True


def jugar_laberinto(nombre, dificultad, puntos):
    """Administra una partida completa del laberinto."""
    vidas_por_dificultad = {
        "cachorros": 4,
        "gato": 3,
        "gatote": 2,
    }
    pasos_por_dificultad = {
        "cachorros": 55,
        "gato": 45,
        "gatote": 35,
    }

    vidas = vidas_por_dificultad[dificultad]
    limite_pasos = pasos_por_dificultad[dificultad]
    laberinto = crear_laberinto(dificultad)
    fila = 0
    columna = 0
    premios = 0
    pasos = 0
    inicial = nombre[0].upper()

    print("\n===== LABERINTO GATUNO =====")
    print("Llega a S para ganar.")
    print("W=arriba, S=abajo, A=izquierda, D=derecha.")
    print("T resta una vida. P suma 5 puntos.")

    while vidas > 0 and pasos < limite_pasos:
        mostrar_laberinto(laberinto, fila, columna, inicial)
        print("Vidas:", vidas, "| Pasos:", pasos, "/", limite_pasos)
        print("Premios:", premios, "| Puntos:", puntos)
        direccion = leer_opcion("Movimiento (W/A/S/D): ", ("w", "a", "s", "d"))

        fila_nueva, columna_nueva, pudo_mover = mover_gato(
            laberinto, fila, columna, direccion
        )
        if not pudo_mover:
            print("No puedes avanzar por ahi.")
            continue

        fila = fila_nueva
        columna = columna_nueva
        pasos += 1
        objeto = laberinto[fila][columna]

        if objeto == "T":
            vidas -= 1
            laberinto[fila][columna] = "."
            print("Una trampa te quito una vida.")
        elif objeto == "P":
            premios += 1
            puntos += 5
            laberinto[fila][columna] = "."
            print("Encontraste un premio: +5 puntos.")
        elif objeto == "S":
            puntos += 20
            print("\n¡Ganaste el laberinto!")
            print("Premios:", premios, "| Total:", puntos)
            return puntos

    print("\nPerdiste el laberinto.")
    print("Te quedaste sin vidas o sin pasos.")
    print("Puntos:", puntos)
    return puntos


def crear_preguntas(dificultad):
    """Crea preguntas de trivia acordes con la dificultad."""
    preguntas_por_dificultad = {
        "cachorros": [
            ["¿Con que parte del cuerpo escucha un gato?", "1=Orejas | 2=Cola | 3=Bigotes", "1", "Orejas"],
            ["¿Como se llama un gato pequeño?", "1=Gatito | 2=Potrillo | 3=Pollito", "1", "Gatito"],
            ["¿Cual de estos es un sonido que hacen los gatos?", "1=Ronroneo | 2=Ladrido | 3=Cacareo", "1", "Ronroneo"],
            ["¿Que usan los gatos para explorar lo que tienen cerca?", "1=Bigotes | 2=Aletas | 3=Plumas", "1", "Bigotes"],
            ["¿Que tipo de animal es un gato?", "1=Mamifero | 2=Reptil | 3=Insecto", "1", "Mamifero"],
        ],
        "gato": [
            ["¿Cuantos dedos suelen tener las patas delanteras de un gato?", "1=Cuatro | 2=Cinco | 3=Seis", "2", "Cinco"],
            ["¿Puede un gato ver en oscuridad absoluta?", "1=Si, siempre | 2=No, necesita algo de luz | 3=Solo de dia", "2", "No, necesita algo de luz"],
            ["¿Por que un gato puede frotar su cara contra objetos?", "1=Para dejar su olor | 2=Para afilar sus dientes | 3=Para refrescarse", "1", "Para dejar su olor"],
            ["¿Que suele comunicar un gato cuando bufa?", "1=Que esta asustado o molesto | 2=Que tiene sueño | 3=Que quiere jugar siempre", "1", "Que esta asustado o molesto"],
            ["¿Que ventaja tienen los bigotes de un gato?", "1=Ayudan a percibir el espacio cercano | 2=Le permiten volar | 3=Le sirven para masticar", "1", "Ayudan a percibir el espacio cercano"],
        ],
        "gatote": [
            [
                "¿A que comportamiento de los gatitos se relaciona el amasado?",
                "1=Al movimiento al mamar | 2=A afilarse las uñas | 3=A regular su temperatura",
                "1",
                "Al movimiento al mamar",
            ],
            [
                "¿Como se llaman los pelos sensoriales del hocico y sobre los ojos?",
                "1=Vibrisas | 2=Plumas | 3=Pelaje",
                "1",
                "Vibrisas",
            ],
            [
                "¿Que organo ayuda a detectar feromonas y otras señales quimicas?",
                "1=Vomeronasal (de Jacobson) | 2=Tiroides | 3=Pituitaria",
                "1",
                "Vomeronasal (de Jacobson)",
            ],
            [
                "¿Que aminoacido esencial necesitan los gatos en su dieta?",
                "1=Taurina | 2=Celulosa | 3=Queratina",
                "1",
                "Taurina",
            ],
            [
                "¿Como se clasifica la dieta natural de los gatos?",
                "1=Carnivora obligada | 2=Herbivora | 3=Omnivora estricta",
                "1",
                "Carnivora obligada",
            ],
        ],
    }
    preguntas = preguntas_por_dificultad[dificultad]
    return random.sample(preguntas, len(preguntas))


def jugar_trivia(nombre, dificultad, puntos):
    """Administra una partida completa de trivia."""
    vidas_por_dificultad = {
        "cachorros": 3,
        "gato": 2,
        "gatote": 1,
    }
    vidas = vidas_por_dificultad[dificultad]
    preguntas = crear_preguntas(dificultad)
    aciertos = 0

    print("\n===== TRIVIA GATUNA =====")
    print("Responde con 1, 2 o 3.")
    print("Completa las 5 preguntas y no pierdas todas tus vidas.")

    for numero in range(len(preguntas)):
        pregunta, opciones, respuesta_correcta, texto_correcto = preguntas[numero]
        print("\nPregunta", numero + 1, "de", len(preguntas))
        print(pregunta)
        print(opciones)
        print("Vidas:", vidas, "| Puntos:", puntos)
        respuesta = leer_opcion("Respuesta: ", ("1", "2", "3"))

        if respuesta == respuesta_correcta:
            aciertos += 1
            puntos += 20
            print("Correcto:", texto_correcto, "+20 puntos.")
        else:
            vidas -= 1
            print("Incorrecto:", texto_correcto)
            if vidas <= 0:
                break

    if aciertos == len(preguntas) and vidas > 0:
        puntos += 30
        print("\n¡Ganaste la trivia!")
        print("Bonus: +30 puntos.")
    else:
        print("\nPerdiste la trivia.")
        print("Aciertos:", aciertos, "de", len(preguntas))

    print("Puntos:", puntos)
    return puntos


def crear_tablero_gato():
    """Crea un tablero vacio de Gato."""
    return [""] * 9


def revisar_ganador_gato(tablero):
    """Devuelve el ganador, empate o None."""
    lineas = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    for a, b, c in lineas:
        if tablero[a] and tablero[a] == tablero[b] == tablero[c]:
            return tablero[a]
    if "" not in tablero:
        return "EMPATE"
    return None


def mostrar_tablero_gato(tablero):
    """Muestra el tablero numerado."""
    print()
    for fila in range(3):
        contenido = []
        for columna in range(3):
            indice = fila * 3 + columna
            contenido.append(tablero[indice] if tablero[indice] else str(indice + 1))
        print(" | ".join(contenido))
        if fila < 2:
            print("-" * 9)
    print()


def movimiento_minimax_gato(tablero, turno):
    """Calcula el mejor movimiento posible con minimax."""
    resultado = revisar_ganador_gato(tablero)
    if resultado == "O":
        return 10
    if resultado == "X":
        return -10
    if resultado == "EMPATE":
        return 0

    puntuaciones = []
    for indice in range(9):
        if tablero[indice]:
            continue
        tablero[indice] = turno
        puntuacion = movimiento_minimax_gato(tablero, "X" if turno == "O" else "O")
        tablero[indice] = ""
        puntuaciones.append(puntuacion)

    return max(puntuaciones) if turno == "O" else min(puntuaciones)


def elegir_movimiento_pc(tablero, dificultad):
    """Elige el movimiento segun la dificultad."""
    libres = [indice for indice, casilla in enumerate(tablero) if not casilla]

    if dificultad == "cachorros":
        return random.choice(libres)

    if dificultad == "gato":
        for simbolo in ("O", "X"):
            for indice in libres:
                tablero[indice] = simbolo
                if revisar_ganador_gato(tablero) == simbolo:
                    tablero[indice] = ""
                    return indice
                tablero[indice] = ""

    mejor_indice = libres[0]
    mejor_puntuacion = -999
    for indice in libres:
        tablero[indice] = "O"
        puntuacion = movimiento_minimax_gato(tablero, "X")
        tablero[indice] = ""
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_indice = indice
    return mejor_indice


def jugar_gato(nombre, dificultad, puntos):
    """Administra una partida de Gato en la consola."""
    tablero = crear_tablero_gato()
    turno = "X"

    print("\n===== GATO (TRES EN RAYA) =====")
    print(nombre + ", eres X y la PC es O.")

    while True:
        mostrar_tablero_gato(tablero)

        if turno == "X":
            movimiento = leer_numero("Elige una casilla (1-9): ", 1, 9)
            indice = movimiento - 1
            if tablero[indice]:
                print("Esa casilla ya esta ocupada.")
                continue
            tablero[indice] = "X"
        else:
            indice = elegir_movimiento_pc(tablero, dificultad)
            tablero[indice] = "O"
            print("La PC eligio la casilla", indice + 1)

        ganador = revisar_ganador_gato(tablero)
        if ganador:
            mostrar_tablero_gato(tablero)
            if ganador == "X":
                puntos += 20
                print("¡Ganaste! +20 puntos.")
            elif ganador == "O":
                print("Gano la PC.")
            else:
                puntos += 5
                print("Empate. +5 puntos.")
            print("Puntos:", puntos)
            return puntos

        turno = "O" if turno == "X" else "X"


def mostrar_menu(nombre, dificultad, puntos):
    """Muestra las opciones principales del juego."""
    print("\nHola,", nombre)
    print("Dificultad:", dificultad, "| Puntos:", puntos)
    print("1. Gato (Tres en raya)")
    print("2. Laberinto gatuno")
    print("3. Trivia gatuna")
    print("4. Salir")
    return leer_opcion("Elige un modo: ", ("1", "2", "3", "4"))


def main(nombre_jugador, dificultad, puntos):
    """Coordina el menu y las partidas."""
    if not nombre_jugador:
        nombre_jugador = leer_texto("\n¿Cómo te llamas, persona curiosa?: ")
    if not dificultad:
        dificultad = elegir_dificultad()

    print("\n===== GATO GATETE =====")
    print("Elige un juego y sigue sus reglas.")
    continuar = True
    partidas = 0

    while continuar:
        opcion = mostrar_menu(nombre_jugador, dificultad, puntos)

        if opcion == "1":
            puntos = jugar_gato(nombre_jugador, dificultad, puntos)
            partidas += 1
        elif opcion == "2":
            puntos = jugar_laberinto(nombre_jugador, dificultad, puntos)
            partidas += 1
        elif opcion == "3":
            puntos = jugar_trivia(nombre_jugador, dificultad, puntos)
            partidas += 1
        else:
            continuar = False
            break

        repetir = leer_opcion("\n¿Volver al menu? (s/n): ", ("s", "n"))
        if repetir == "n":
            continuar = False

    print("\nGracias por jugar,", nombre_jugador)
    print("Puntaje final:", puntos)
    print("Partidas realizadas:", partidas)
    print("Hecho por: Sarah Lim0n y Lizbeth Osiris")


if __name__ == "__main__":
    main("", "", 0)
