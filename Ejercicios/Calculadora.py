operacion = input("Que operacion deseas realizar Suma(+)\Resta(-)\Division(/)\Multiplicación(*)")
v1 = int(input("Primer numero"))
v2 = int(input("segundo numero"))
resultado = int
if operacion == "+":
    resultado = v1 + v2
    print("Resultado: ",resultado)
else:
    if operacion == "-":
        resultado = v1 - v2
        print("Resultado: ", resultado)
    else:
        if operacion == "/":
            resultado = v1 / v2
            print("Resultado: ", resultado)
        else:
            if operacion == "*":
                resultado = v1 * v2
                print("Resultado: ",resultado)