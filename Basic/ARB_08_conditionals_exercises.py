# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
el_num = int(input("Pon tu edad.: "))
if el_num > 0:
    print("El número es positivo")
elif el_num == 0:
    print("El número es cero")
else:
    print("El número es negativo")

# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o más) o menor de edad.
if el_num < 18 and el_num >= 0:
    print("Eres menor de edad.")
elif el_num >= 18:
    print("Eres mayor de edad")
else:
    print("No has nacido o has muerto.")

# 3. Escribe un programa que verifique si una cadena de texto está vacía y muestre un mensaje en consecuencia.
el_texto = str(input("Escribe algo o no.: "))
if el_texto == "":
    print("No has escrito nada.")
else:
    print("Tu texto es: " + el_texto)

# 4. Crea un programa que solicite dos números al usuario y compare cuál es mayor. Si son iguales, muestra un mensaje indicando la igualdad.
un_num = int(input("Escríbeme un numero.: "))
otro_num = int(input("Escríbeme otro numero.: "))
if un_num == otro_num:
    print("Son números iguales.")
elif un_num > otro_num:
    print("El primer numero es mayor.")
elif un_num < otro_num:
    print("El segundo numero es mayor.")
else:
    print("No es un numero.")

# 5. Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
print("El resto de " + str(el_num) + " entre 3 es: " + str((el_num % 3)))
print("El resto de " + str(el_num) + " entre 3 es: " + str((el_num % 5)))

if el_num % 3 == 0 and el_num % 5 == 0:
    print(str(el_num) + " Es divisible entre 3 y 5 al mismo tiempo.")
else:
    print(str(el_num) + " No es divisible entre 3 y 5 al mismo tiempo.")

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
if el_num % 2 == 0:
    print(str(el_num) + " El número es par")
else:
    print(str(el_num) + " Es impar.")

# 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
if el_num >= 18:
    print("Puedes votar")
elif el_num >= 16 and el_num <= 17:
    print("Puedes votar si tienes una autorización de un representante legal.")
else:
    print("No puedes votar.")

# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
tu_contraseña = input("Escribe (noRte) u otra cosa o no.: ")
if tu_contraseña == "noRte":
    print("¡Bienvenido!")
else:
    print("Contraseña incorrecta.")
# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
if el_num >= 10 and el_num <= 20:
    print("El número está entre 10 y 20.")
# 10. Escribe un programa que simule un semáforo: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.
semaforo = input("Escribe Rojo, Amarillo, Verde.: ")
semaforo = semaforo.capitalize()
print(semaforo)
if semaforo == "Rojo":
    print("Detente.")
elif semaforo == "Amarillo":
    print("Precaución has de detenerte.")
elif semaforo == "Verde":
    print("Puedes pasar.")
else:
    print("No es un color de semaforo.")