# 1.- Declara y asigna valores a las siguientes variables:
# 	name: una cadena que contenga tu nombre.
# 	age: un número entero que represente tu edad.
# 	height: un número flotante que represente tu altura.
# 	Imprime cada variable en una li­nea separada.

nombre = "Antonio"
edad = 43
altura = 1.70
print(nombre)
print(edad)
print(altura)

# 2 .- Convierte la variable edad de entero a cadena y concatena con un texto que diga cuantos años tienes.
edad = str(edad)
print(type(edad))
print(nombre, "tu edad es:", edad+".")

# 3 .- Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprimela.
is_student = True
print(is_student)

# 4 .- Usa la función len() para calcular cuantos caracteres tiene tu nombre completo, almacenado en una variable.
longitud = len(nombre)
print(longitud)

# 5 .- Declara tres variables en una sola lí­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
primer_apellido = "Romero"
segundo_apellido = "Bravo"
ciudad = "Granada"
print("Te llamas:", nombre, primer_apellido, segundo_apellido, "y vives en:", ciudad+".")

# 6 .- Usa la función input() para solicitar al usuario su color favorito y almacenalo en una variable color. Luego, imprime el valor ingresado.
print("¿Cual es tu color favorito?")
su_color = input()
print("Tu color favorito es el", su_color)

# 7 .- Declara una variable fruit e inicializala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "Manzana"
print(fruit)
fruit = "Se puede cambiar la fruta."
print(fruit)

# 8 .- Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprimela.
decimal = 8.6
decimal = round(decimal, None)
print(decimal)

# 9 .- Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address_len = "Calle Lanzarote"
address_len = len(address_len)
print(address_len)

# 10 .- Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone: int = 958901858
phone = "Python no es un lenguaje fuertemente tipado."
print(phone)
print(type(phone))
