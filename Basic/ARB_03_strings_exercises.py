# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
print("Hola" + "Python")

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
print("Esta es mi \ncadena con salto \nde lineas.")

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre, apellido, edad = "Antonio", "Romero", 43
print(f"Hola, soy {nombre} {apellido} y tengo {edad} años.")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
palabra = "Python"
primera = palabra[0]
print(primera)
segunda = palabra[1]
print(segunda)
segunda = palabra[2]
print(segunda)
tercera = palabra[3]
print(tercera)
cuarta = palabra[4]
print(cuarta)
quinta = palabra[5]
print(quinta)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
extraer = "Programación"
parte = extraer[3:7]
print(parte)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
# Utilizo la variable (palabra) del ejercicio 5
print(palabra[::-1])

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
cadena = "aprendiendo python"
print(cadena.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
print(cadena.count("n"))
print(cadena) #Compruebo que no se ha cambiado a mayúsculas.

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
cadena_num = "12345"
print(cadena_num.isdecimal())

print("python".isnumeric())