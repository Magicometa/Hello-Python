# 1. Crea un set con los números del 1 al 5 e imprímelo.
es_set = {1, 2, 3, 4, 5}
print(es_set)
print(type(es_set))

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.
es_set.add(6)
print(es_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
es_set.add(5) #no añade el número ya que no permite elementos repetidos.
print(es_set)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in es_set)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
es_set.remove(4)
print(es_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.
es_set.clear()
print(es_set)

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.
fruta = {"manzana", "naranja", "plátano"}
fruta = list(fruta)
print(fruta[0])
print(type(fruta))

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.
set_uno = {1, 2, 3}
set_dos = {4, 5, 6}
set_unido = set_uno.union(set_dos)
print(set_unido)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.
di_uno = {1, 2, 3, 4}
di_dos = {3, 4, 5, 6}
di_resultado = di_uno.difference(di_dos)
print(di_resultado)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.
my_set = {50, 60}
del my_set
# print(my_set) dará error por que la variable se ha borrado por completo.

otro_set = {1, 1, 2, 2, 3, 3}
print(len(otro_set))