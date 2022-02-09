#Booleanos
#Dos tipos
#True y False

#True -> 1
#False -> 0

variable1=True
variable2=False

print(type(variable1))

print(variable1.bit_length())

## Operadores
#Asignación -> =
#Aritméticos
# #Strings -> concatenación (+)

#Asignación Complementarios
x=4
x+=5 #se le suma 5 a x
print(x) 
x**=2
print(x) 

#Operadores Lógicos
#Conjunción -> y    (and)
print(variable1 and variable2)
print(True and True)
print(False and False)

#Disyunción -> o    (or)
print("OR")
print(variable1 or variable2)
print(False or False)

#Negación -> not
print(not variable1)
print(not variable2)

# Ejemplo
print("1. ",4 ^ 5)
print("2. ",True and True)

'''
#Operadores Bit a Bit
# AND
print(True & True)
# OR
print(4 | False)
#XOR
print(4 ^ 5)
# NOT
print(~ False)
#Desplazamiento Bit a Bit a la derecha
print(True >> False)
#Desplazamiento Bit a Bit a la izquierda
print(True << False)
'''
#Ejemplo bit a bit
var1=2
var2=3
var3=5
print("Probando los binarios")
print(var1 & var2)
print(var1 | var2)
print(var1 ^ var2)
print(~var1)
print(var1 >> var2)
print(var1 << var2)




#Operadores de Pertenencia
#Identidad

