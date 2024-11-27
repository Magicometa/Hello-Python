# 1. Crea una lista con los números del 1 al 5 e imprímela.
lista_num = [1, 2, 3, 4, 5]
print(lista_num)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista_dos = [10, 20, 30, 40, 50]
print("El tercer elemento es:", lista_dos[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
lista_num.append(6)
print(lista_num)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
lista_dos.insert(1, 15)
print(lista_dos)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
lista_tres = [10, 20, 30, 30, 40, 50]
lista_tres.remove(30)
print(lista_tres)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
lista_cuatro = [1, 2, 3, 4, 5]
eliminado = lista_cuatro.pop(-1)
print(lista_cuatro)
print(eliminado)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
lista_cinco = [100, 200, 300, 400, 500]
lista_cinco.reverse()
print(lista_cinco)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
lista_seis = [3, 1, 4, 2, 5]
lista_seis.sort()
print(lista_seis)
lista_seis.sort(reverse = True)
print(lista_seis)

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
lista_mitad_uno = [1, 2, 3]
lista_mitad_dos = [4, 5, 6]
lista_unida = lista_mitad_uno + lista_mitad_dos
print(lista_unida, "Lista unida.")

# 10. Crea una sub lista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
sub_lista = lista_dos.copy()
sub_lista.remove(15)
print(sub_lista[1:3])