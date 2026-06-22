import random

# INICIO: Inicializar Variables
marcador_humano = 0
marcador_cpu = 0
opciones = ["Piedra", "Papel", "Tijera"]

# Bucle principal del juego
while True:
    # PEDIR ACCIÓN O JUGADA
    jugada_humano = input("Ingrese 'Piedra', 'Papel', 'Tijera' o 'Salir': ")

    # ¿Qué acción o jugada se ingresó?
    if jugada_humano == "Salir":
        # MOSTRAR PUNTUACIÓN FINAL y salir del bucle (FIN)
        print(f"Final: Humano [{marcador_humano}] - CPU [{marcador_cpu}]")
        break
        
    elif jugada_humano in opciones:
        # TURNO DE CPU
        jugada_cpu = random.choice(opciones)
        
        # MOSTRAR JUGADAS
        print(f"Humano: [{jugada_humano}] vs CPU: [{jugada_cpu}]")
        
        # ¿Empate?
        if jugada_humano == jugada_cpu:
            print("Empate")
        else:
            # EVALUAR REGLAS DE VICTORIA
            if (jugada_humano == "Piedra" and jugada_cpu == "Tijera") or \
               (jugada_humano == "Papel" and jugada_cpu == "Piedra") or \
               (jugada_humano == "Tijera" and jugada_cpu == "Papel"):
                
                # Jugador gana
                marcador_humano += 1
                print("¡Ganaste!")
            else:
                # Jugador pierde (Gana CPU)
                marcador_cpu += 1
                print("Perdiste")
                
        # MOSTRAR MARCADOR ACTUAL
        print(f"Humano [{marcador_humano}] - CPU [{marcador_cpu}]\n")
        
    else:
        # Cualquier otra cosa
        print("Entrada inválida. Reintenta.\n")