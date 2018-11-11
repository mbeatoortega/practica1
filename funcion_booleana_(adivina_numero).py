numero_ganador = 8

numero_usuario = int (input("adivina el numero ganador:"))

if numero_ganador == numero_usuario:
    print("!felicidades has Ganado!")

else:

    numero_usuario = int(input("intenta otra vez "))

    if numero_ganador == numero_usuario:
        print("!felicidades has Ganado!")

    else:
        numero_usuario = int(input("intenta otra vez "))

        if numero_ganador == numero_usuario:
            print("!felicidades has Ganado!")

        else:
            numero_usuario = int(input("intenta otra vez "))

            if numero_ganador == numero_usuario:
                print("!felicidades has Ganado!")

            else:
                print("has perdio")