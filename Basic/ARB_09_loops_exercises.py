# 1. Usa un bucle while para imprimir los números del 1 al 10.
cuenta = 0
while cuenta < 10:
    cuenta += 1
    print(cuenta)
print("Fin de while. \n")

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
bucle = [10, 20, 30, 40, 50]
for mirar in bucle:
    print(mirar)
print("Fin de for. \n")

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 20 e imprime el resultado.
cuenta = 0
sumatoria = 0
while cuenta <= 20:
    print(f"Voy a sumar {cuenta} + {sumatoria}.")
    sumatoria = cuenta + sumatoria
    print(sumatoria)
    cuenta += 1
else:
    print(f"El valor de la sumatoria de 20 números es: {sumatoria}")
print("Fin de sumatoria. \n")

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
palabra = "Python"
for deletrea in palabra:
    print(deletrea)
print("Fin deletrea. \n")

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
buscar = 1
while (buscar & 7) != 0:
    buscar += 1
else:
    print(f"{buscar - 1} es divisible entre 7. \n")

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
disc = {"name": "Brais", "age": 37, "country": "Galicia"}
# Imprime la clave
for claves in disc:
    print(claves)
else:
    print("Fin de las claves. \n")

# Imprimir valores
for claves, valor in disc.items():
    print(valor)
else:
    print("Fin de valores. \n")

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
pares = 1
while pares <= 20:
    if pares % 2 == 0:
        print(f"{pares} es par.")
    pares += 1
else:
    print("Fin de pares. \n")

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for inverso in range(10, 0, -1):
    print(inverso)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
treinta = [30, 10, 30, 20, 30, 40]
contador = 0
for repetido in treinta:
    if repetido == 30:
        contador += 1
else:
    print(f"El número 30 se repite {contador} veces. \n")

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
nombres = ["Jose", "Mauricio", "Pepe", "brais", "Pepito", "menganico"]
for te_vi in nombres:
    print(te_vi.capitalize())
    if te_vi.capitalize() == "Brais":
        print(f"Te encontré {te_vi.capitalize()} detengo el bucle. \n")
        break
