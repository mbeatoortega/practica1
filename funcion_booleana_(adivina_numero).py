print("Bienvenidos a adivina el numero")
print("Es sencillo consiste en adivinar el numero ganador en 4 intentos ")
numero_ganador = 8

numero_usuario = int (input("adivina el numero ganador:"))

if numero_ganador == numero_usuario:
    print("!felicidades has Ganado!")

else:
    print("te quedan 3 intentos")
    numero_usuario = int(input("intenta otra vez "))

    if numero_ganador == numero_usuario:
        print("!felicidades has Ganado!")

    else:
        print("te quedan 2 intentos")
        numero_usuario = int(input("intenta otra vez "))

        if numero_ganador == numero_usuario:
            print("!felicidades has Ganado!")

        else:
            print("te quedan 1 intentos")
            numero_usuario = int(input("intenta otra vez "))

            if numero_ganador == numero_usuario:
                print("!felicidades has Ganado!")

            else:
                print("has perdio")