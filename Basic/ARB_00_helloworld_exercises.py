# 1.- Imprimir "Â¡Hola Mundo!" por consola.
# 2.- Escribir un comentario de una sola linea explicando que hace el código del Ejercicio 1.
print("\"Â¡Hola Mundo!\"") #Imprime "Â¡Hola Mundo" literalmente.

# 3.- Imprime tu nombre y edad en la misma linea utilizando la función print.
print("Antonio de 43 años.")

# 4.- Usa la función type() para imprimir el tipo de dato de una cadena de texto, un numero entero y un numero decimal.
print(type("Esto es un texto.")) # tipo texto (str)
print(type(5)) # tipo entero (int)
print(type(5.8)) #tipo decimal (float)

# 5 .- Escribe un comentario en varias lineas explicando que son los tipos e datos en Python.
"""
Un tipo de dato hace referencia a la sintaxis que puede utilizar el código
que se pueden clasificar en varios tipos según su funcionamiento, como por ejemplo si es texto, números, booleanos, fechas, entre otros.
"""

# 6 .- Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
print("Hola""Mundo")
print("Hola"+"Mundo2")

# 7 .- Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
mi_nombre = "Antonio"
mi_edad = 43
print(mi_nombre, mi_edad)

# 8 .- Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
print("Escribe tu nombre y pulsa \"Enter\"")
tu_nombre = input()
print("Hola", tu_nombre)

#9 .- Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
#10 .- Comenta el código del ejercicio 9, y explica que hace cada linea usando comentarios de una sola linea.
print(type(5+6)) #Imprime el tipo de dato del resultado de una suma.