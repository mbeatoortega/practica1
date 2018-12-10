print("Convertidor de grados")
operacion = int(input("Celsius to Fahrenheit(1)  \   Fahrenheit to Celsius(2)"))

v1 = int(input("Ingrese valor "))
result = int
if operacion == 2:
    result = (v1 -32) *5/9
    print("{}Cº".format(result))

else:
    result = (v1*9/5) + 32
    print("{}F".format(result))