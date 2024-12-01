# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.
el_dic = {
    "name":"Antonio",
    "age":43,
    "country":"Granada"
    }
print(el_dic)

# 2. Accede al valor de la clave name en el diccionario.
print(el_dic["name"])

# 3. Añade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
el_dic["job"] = "programador"
print(el_dic)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
el_dic["age"] = 38
print(el_dic)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del el_dic["age"]
print(el_dic)

# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
cuadrados = {1:1, 2:4, 3:9, 4:16, 5:25}
print(cuadrados)
print(cuadrados.items())

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.
print("age" in el_dic)

# 8. Imprime solo las claves del diccionario.
print(el_dic.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.
print(list(el_dic))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
nuevo_dic = {}
nuevo_dic = nuevo_dic.fromkeys(("name", "age", "job"))
print(nuevo_dic)
nuevo_dic = nuevo_dic.fromkeys(nuevo_dic, "Desconocido")
print(nuevo_dic)
