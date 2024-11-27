# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
tupla = (10, 20, 30, 40, 50)
print(tupla)
print(type(tupla))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
otra_tupla = (100, 200, 300, 400, 500)
print(otra_tupla[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
segunda_tupla = (1, 2, 3)
# segunda_tupla[0] = 100 Error
print(segunda_tupla)

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
contar_tupla = (1, 2, 3, 3, 4, 5, 3)
print(contar_tupla.count(3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
coincidencia = ("Java", "Python", "JavaScript", "python")
print(coincidencia.index("python")) # Reconoce mayúsculas

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tupla_uno = (1, 2, 3)
tupla_dos = (4, 5, 6)
suma_tuplas = tupla_uno + tupla_dos
print(suma_tuplas)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
original = (10, 20, 30, 40, 50)
sub_lista = original[1:4]
print(sub_lista)

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
colores = ("rojo", "verde", "azul")
colores = list(colores)
print(colores)
colores[1] = "amarillo"
print(colores)
colores = tuple(colores)
print(type(colores))

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (100, 200)
print(my_tuple)
del my_tuple
# print(my_tuple) Da error porque se ha eliminado

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
unico = (1000,)
print(type(unico))
print(1000 in unico)