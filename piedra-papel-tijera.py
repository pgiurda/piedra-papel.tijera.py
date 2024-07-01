

nombre1 = input("¿Como se llamara el jugador 1?: ")
nombre2 = input("¿Como se llamara el jugador 2?: ")

cant_intentos = 3

while cant_intentos > 0:
    jugador1 = print("Hola", nombre1.capitalize()),input("¿Que eliges? ¿Piedra, papel o tijera?: ")

    jugador2 = print("Hola", nombre2.capitalize()),input("¿Que eliges? ¿Piedra, papel o tijera?: ")

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    if jugador1 == jugador2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print('Ha ganado: ', nombre1.capitalize())
    else:
        print('Ha ganado: ', nombre2.capitalize())
    
    cant_intentos -= 1
    print("intentalo otra vez, te quedan:",cant_intentos, "intentos")

if not cant_intentos > 0:
    print("El juego se ha terminado")