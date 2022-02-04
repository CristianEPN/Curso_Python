#Programa que permita resolver una ecuación de segundo grado
#ax^(2)+bx+c=0 //a, b y c son numeros enteros
#Pedir al usuario que ingrese valores de a, b y c
# Imprimir en consola la ecuación de segundo grados
# Mostrar las dos soluciones x1, x2
import math

print("\t RESOLUCION DE ECUACIONES DE SEGUNDO GRADO \n")
print("\t La ecuación tendra la forma: ax^(2)+bx+c=0 \n")
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))
print(a,"x^(2) + ",b,"x",c,"=0")
x1=int((-b+math.sqrt((b**2)-(4*a*c))))/(2*a)
x2=int((-b-math.sqrt((b**2)-(4*a*c))))/(2*a)

print("X1 = ",x1,"\n","X2 = ",x2)



