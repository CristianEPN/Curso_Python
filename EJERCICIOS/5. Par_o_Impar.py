#Usuario ingresa un numero y diremos si es par o impar

numero=int(input("Ingrese un número: "))
if numero%2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")

if numero>0:
    print("Es un núumero mayor a cero")
else:
    print("Es un número menor a cero")