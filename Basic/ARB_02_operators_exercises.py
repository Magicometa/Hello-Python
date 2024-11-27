# 1. Realiza las siguientes operaciones aritméticas:
# •	Suma: 15 + 25
print(15 + 25)
# •	Resta: 50 - 22
print(50 - 22)
# •	Multiplicación: 8 * 7
print(8 * 7)
# •	División: 100 / 20      
print("La division da:", 100 / 20)

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.
remainder = (37 & 5)
print("El resto es:", remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”. Imprime el resultado.
print(str(7) + " es mi numero favorito.")

# 4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
print("Python, " * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
resultado = a > b
print(resultado)

# 6. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y < y explica cuál tiene mayor orden alfabético.
comp_mayor = "apple" > "banana"
print(comp_mayor)
comp_menor = "apple" < "banana"
print(comp_menor)

# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
es_verdad = ((10 > 5) and (10 < 20))
print(es_verdad, ", tiene que dar True si los dos son verdaderos.")

# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.
sera_verdad = ((7 < 3) or (7 > 5))
print(sera_verdad, ", tiene que dar True si uno es verdadero.")

# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?
print(not(15 > 20), ", Da True porque invierte el resultado que es: False.")

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
print((((5 * 3) + 2) > 10) and (((5 * 3) + 2) < 20), ", Da True con el operador and")