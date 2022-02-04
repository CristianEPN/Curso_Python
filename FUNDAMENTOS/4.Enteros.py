'''
#Enteros -> Int
#Conversiones de datos

num1=input("Ingresa un número: ")     #num1 tipo string
print(type(num1))
num1=int(num1)          #Int toma un string y lo cambia a entero
print(num1+20)

#En una sola linea de código, se toma la entrada de input y lo convierte a entero
num2=int(input("Ingrese otro número: "))
print(num2+2)

num3=int("XD")          #Error imposible transformar
print(num3)

num4=int(True)          #True=1     False=0
print(num4)
'''
#Importaciones
import math
#Operadores Numericos
a,b=4,6

print("\t Operaciones Númericas\n")
#-> Suma
print("Suma: ",a+b)
#-> Resta
print("Resta: ",a-b)
#-> Multiplicación
print("Multiplicación: ",a*b)
#-> División
print("Division: ",a/b)     #Siempre devolvera un flotante
#-> Potencia
print("Potencia: ",2**3)
#-> Raiz Cuadrada
print("Raiz con potencia: ",64**(1/2))
print("Raiz Cuadrada: ", math.sqrt(64))
#-> Módulo
print("Modulo: ",b%a)
#-> Division Entera
print("Division Entera: ",10//3)

# *******************************************
# Floats -> float, consideraciones separacion con el -
# *******************************************
numeroFlotante=float(input("Ingrese un numero decimal"))
print(numeroFlotante)
