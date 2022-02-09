#Strings -> str     = Dato indexable, tipo de dato inmutable
#Inmutable -> no acepta asignación

#Asignación de una unica linea
x="Hola"
y="con todos"

#String de varias lineas
texto='''Libro Quijote
Cervantes
Es un pueblo de la mancha....
Ahi está el molino
'''
print(texto)

texto2 = '''
Primer \t linea
Segunda \n linea
Tercera
'''

#print(texto2)
cadena1="Python "
cadena2="es un lenguaje"
numero1=8.5
print(type(numero1))
print(cadena1 + cadena2, "Interpretado", numero1)

cadena3=cadena1+cadena2
print(cadena3)

#Clases
#Atributos
#Métodos -> Funciones
#Las instancias tienen los métodos

#Formatos Strings
nombre="Alejandro"
edad=19
ira=32
universidad="EPN"
#1. Basado en Variables
print(f"1. Hola mi nombre es {nombre} y mi edad es {edad} y tengo un ira de {ira}")

#2. Llama al método de la clase string
print("2. Hola mi nombre es {} y mi edad es {} y tengo un ira de {}".format(nombre,edad,ira))

#3. Llamada al método de la clase format pero indicando la posición
print("3. Hola mi nombre es {0} y mi edad es {1} y tengo un ira de {2}".format(nombre,edad,ira))

#3.1 Con repeticion
print("3.1. Hola, mi nombre es {0}, estudio en la {1} y asisto al curso de Ingles de la {1}".format(nombre,universidad))

#4. Formated string con reasignación de variables
print("4. Hola mi nombre es {variableNombre} y mi edad es {variableEdad} y tengo un ira de {variableIra}".format(variableNombre="Alejandro",variableEdad=edad,variableIra=ira))
#Objeto -> str
#Atributos -> privados
#Metodo -> format

#2: Indexación
#"Python"
#|0|1|2|3|4|5|
cadenaTexto="Este es un curso de Programación"
print(cadenaTexto[2])

#Range -> rango
print(len("Hola"))

#0 -> H
#1 -> O
#2 -> L
#3 -> A

print(len(cadenaTexto))
print(cadenaTexto[0])   #E
#error print(cadenaTexto[32])
# error print(cadenaTexto[31])

#Cuando se utiliza los número positivos, empieza a contar de adelante hacia atras empezando desde 0
#Cuando se utiliza los numeros negativos, empieza a contar de atras hacia adelante desde -1
print(cadenaTexto[-1])
print(cadenaTexto[-32])

print(cadenaTexto[1]+cadenaTexto[8]+cadenaTexto[13])

# error -> cadenaTexto[0]="A"
letra=cadenaTexto[0]
print(letra)
letra="A"
print(letra)

#Indexación en rangos
#[valorIncluido:valorExcluido]
#[0,2)
print(cadenaTexto[0:2])
print(cadenaTexto[0:10])
print(cadenaTexto[2:20])
print(cadenaTexto[2:20:5])  #Agregar un salto
#Indice hasta el final
print(cadenaTexto[2:])
#Desde el comienzo hasta el indice
print(cadenaTexto[:3])  #Est
#Necesito todo el contenido
print(cadenaTexto[:])
print(cadenaTexto[::])

#Ejercicio: Invierta todo la variable
cadenaInvertida=cadenaTexto[::-1]
print(cadenaInvertida)

#Funciones en Python
print(cadenaTexto.upper()) #PONE TEXTO EN MAYUSCULAS
print(cadenaTexto.lower())  #PONE TEXTO EN minusculas
print(cadenaTexto.capitalize()) #PONE LA PRIMERA LETRA EN MAYUSCULAS
#Encontrar algo en tu cadena de texto
#Si encuentra devuelve el indice de la primera coincidencia
print(cadenaTexto.find("curso"))
print("Animales: tigre".find("tigre"))
#Si no encuentra me devuelve -1
print("Animales: tigre".find("perro"))

cadenaTexto2="Los niños juegan en el parque"
#Validar si empieza con ...
print(cadenaTexto2.startswith("Los"))
print(cadenaTexto2.startswith("Las"))
print(cadenaTexto2.endswith("parque"))
print(cadenaTexto2.startswith("cine"))

print(cadenaTexto2.replace("niños","niñas").replace("Los","Las"))
