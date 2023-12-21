#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

def obtener_opcion_oponente():
    opciones = ['piedra', 'papel', 'tijeras']
    return random.choice(opciones)

def determinar_ganador(jugador, oponente):
    if jugador == oponente:
        return 'Empate'
    elif (
        (jugador == 'piedra' and oponente == 'tijeras') or
        (jugador == 'tijeras' and oponente == 'papel') or
        (jugador == 'papel' and oponente == 'piedra')
    ):
        return '¡Ganaste!'
    else:
        return '¡Perdiste!'

def jugar():
    puntaje_jugador = 0

    while True:
        print("\n--- Piedra, Papel o Tijeras ---")
        jugador = input("Elige piedra, papel o tijeras: ").lower()

        if jugador not in ['piedra', 'papel', 'tijeras']:
            print("¡Opción no válida! Por favor, elige piedra, papel o tijeras.")
            continue

        oponente = obtener_opcion_oponente()

        print(f"\nTu oponente eligió: {oponente}")
        resultado = determinar_ganador(jugador, oponente)
        print(f"Resultado: {resultado}")

        if resultado == '¡Ganaste!':
            puntaje_jugador += 1
        elif resultado == '¡Perdiste!':
            puntaje_jugador -= 1

        print(f"\nPuntaje actual: {puntaje_jugador}")

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("¡Gracias por jugar! Puntuación final:", puntaje_jugador)
            break

if __name__ == "__main__":
    jugar()
