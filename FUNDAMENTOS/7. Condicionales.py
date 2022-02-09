#Si, sino, entonces
#If, else, elif

variable1=True
variable2=False

#Operador
# 1. (==) comparación

#print(1 == 1)
#print("Hola"=="Hola")

if variable1 and variable2 -- True:
    print("La exporesión es verdadera")
else:
    print("La expresión es falsa")

#Comprobaciones

texto="Alejandro"
#Python se puede omitir la comparación a verdadero
#if texto.startswith("A") == True
#Es igual a escribir
if texto.startswith("A"):
    print("Tu nombre empieza con A")
elif texto.startswith("B"):
    print("Tu nombre empieza con la B")
else:
    print("Tu nombre no empieza con la letra A ni con la B")

#Otro tipo de comparaciones
print(10>=10)
print(20<30)
print(500 != 200)
print(200 != 200)
print("Cristian" != "Alejandro")

x=10
print(0<x<12)
print(4<5<8<200)

print("A" > "B")
print("oso" <= "oso")
