# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningún nombre, debe saludar diciendo "Hola, desconocido".
def personalizado(nombre):
    print(f"Hola {nombre}. \n")
personalizado(input("Escribe tu nombre.: "))

# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
def multiplicar(n_uno, n_dos):
    return n_uno * n_dos
print(multiplicar(5, 8))
print("\n")

# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(n_n):
    n_n = int(n_n)
    if n_n % 2 == 0:
        return True
    else:
        return False
devuelto = is_even(input("Escribe un numero.: "))
print(f"Tu numero es {devuelto}. \n")

# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_up(texto):
    mayusculas = ""
    for up in texto:
        mayusculas += up.upper()
    return mayusculas
ver = convert_up(input("Escribe una palabra.: "))
print(f"Tu palabra en mayúsculas: {ver}. \n")

# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary (*suma):
    numeros = 0
    for sumalo in suma:
        numeros += sumalo
    return (f"La sumatoria es: {numeros}")
print(arbitrary(5, 6, 10))

# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
tu_nombre = {
    "nombre" : "Josemi",
    "apellido" : "Delgado"
    }
def full_greeting (diccionario):
    nom = diccionario["nombre"]
    ap = diccionario["apellido"]
    print(f"Hola {nom} {ap}. \n")
full_greeting(tu_nombre)

# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
cuadrado = (5, 2)
def power (base, exponente):
    return base**exponente
print(power(cuadrado[0], cuadrado[1]))
print("\n")

# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average (*calcular):
    sumado = 0
    for calculo in calcular:
        sumado += calculo
        print(sumado)
    return (f"La media de los numeros es: {sumado/len(calcular)}")
print(calculate_average(2, 4, 6))
print("\n")


# 9. Crea una función llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_chrt (texto):
    return (f"Tu texto tiene {len(texto)} letras.")
print(count_chrt(input("Escribe un texto.: ")))
print("\n")

# 10. Escribe una función llamada "display_messages" que reciba un número indefinido de cadenas y las imprima en mayúsculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*textos):
    for texto in textos:
        print(texto.upper())
display_messages("hola", "mundo", "esto es una prueba")