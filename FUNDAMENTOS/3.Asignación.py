#Asignacion = Drle un valor a ese espacio
# =

x = 5
print("El valor de la variable X es: ",x)

#Asignacion sin valor
#None = no tiene ningun dato
variable = None
print(type(variable))
print("El valor de la variable es: ",variable)

#Inicializar variable Y con el valor de 10
y = 10          #Variable vale 10
print(y)
#multiplicar por dos
y = y*2         #10 * 2 = 20 (valor de y = 20)
print(y)
#multiplicar por dos
print(y*2)      #40
print(y)        #20

#Asignacion con diferentes tipos
y = "Saludo"
print(y)

#Multiples Asignaciones
#Crear variables A y B con los valores de 2 y 3
a, b, saludo=2, 3, "Hola"
print(a*b)
print(saludo)

#Asignacion del valor de una variable a otra variable
#Se coloca el contenido en ese instante
saludo2 = saludo
print(saludo2)
saludo="Buenas Tardes"
print(saludo2)

#Ejercicio
x1=4
y1=x1+1
x1=2
print(x1,y1)

#Ejercicio 2
#Errores en la asignacion
x2, y2=10, 11
z2=x2
y2=z2+2
print(x2," ",y2," ",z2)

#Apuntar a Nulo
# hex -> variable

x2, y2=z3+1, 5          #error por que es una variable mas no un valor
x2, x2=1,2              #no es error por que son valores asignadas a variables