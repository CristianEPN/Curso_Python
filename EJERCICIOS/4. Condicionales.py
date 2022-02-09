#Capicuas
#Palindromos

#Solicitar al usuario que ingrese por teclado un texto, le vamos a indicar si lo ingresado es o no un palindromo

print("\tIdentificador de PALINDROMOS")
texto=str(input("Ingrese una palabra: "))
print("Palabra de izquierda a derecha: "+texto)
print("Palabra de derecha a izquierda: "+texto[::-1])

if texto == texto[::-1]:
    print("Ingresaste un Palindromo")
elif texto.lower() == texto[::-1].lower():
    print("Palindromo, Ignorando las mayúsculas")
elif texto.replace(" ","") == texto[::-1].replace(" ",""):
    print("Palindromo, Ignorando los espacios")
elif texto.lower().replace(" ","") == texto[::-1].lower().replace(" ",""):
    print("Palindromo, Ignorando los espacios y las mayusculas")
else:
    print("No ingresaste un Palindromo")

