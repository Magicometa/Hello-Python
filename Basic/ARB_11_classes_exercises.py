# 1. Crea una clase llamada "Animal" que tenga una propiedad "species" y un método "make_sound" que imprima un sonido genérico.
class Animal:
    def __init__(self, species):
        self.species = species
    
    def make_sound(self):
        if self.species == "Cerdo":
            print(f"El {self.species} hace oinc! oinc!")
        elif self.species == "Gallo":
            print(f"El {self.species} hace cockorocock!!")
        else:
            print(f"El {self.species} hace un sonido de {self.species}.")




el_cerdo = Animal("Cerdo")
el_cerdo.make_sound()

# 2. Modifica la clase "Animal" para que reciba la especie al crear un objeto y almacénala en una propiedad pública. Añade el método "make_sound" que imprima un sonido dependiendo de la especie.
el_gallo = Animal("Gallo")
el_gallo.make_sound()
el_perro = Animal("Perro")
el_perro.make_sound()

# 3. Crea una clase llamada "Car" con las propiedades públicas "brand" y "model". Además, debe tener una propiedad privada "_speed" que inicialmente será 0.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10
    def brake(self):
        self.__speed -= 10

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
coche = Car("BMW", "Z4")
coche.accelerate()
#print(f"El {coche.brand} {coche.model} va a {coche.__speed}km/H.") # No se puede imprimir la velocidad por que es privada.
coche.brake()
#print(f"El {coche.brand} {coche.model} va a {coche.__speed}km/H.") # No se puede imprimir la velocidad por que es privada.

# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    def el_autor(self):
        print(self.__author)

    def cambiar(self, nuevo):
        self.title = nuevo

libro = Book("Calambre", "Carlos")
print(libro.title)
libro.el_autor()
libro.cambiar("Esperanza")
print(libro.title)

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.
class Estudiante:
    def __init__(self, nombre, apellido, notas):
        self.nombre = nombre
        self.apellido = apellido
        self.notas = notas

    def media(self):
        sumar = 0
        for valor in self.notas:
            sumar += valor
        print(f"La media de {self.nombre} es {sumar / len(self.notas):.2f}")

alumno = Estudiante("Jose", "Miguel", [5.6, 8, 9.4])
alumno.media()

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def ingreso(self, agregar):
        self.balance += agregar
        print(f"Su balance actual es de {self.balance} euros.")
    
    def retirar (self, sacar):
        if (self.balance - sacar) <= 0:
            print(f"Su balance es de {self.balance} Euros.\nNo tiene suficientes fondos para retirar {sacar} Euros.")
        else:
            self.balance -= sacar
            print(f"A retirado {sacar} Euros.\nEn la cuenta le quedan {self.balance} Euros.")

usuario = BankAccount("Maria", 100)
usuario.ingreso(1000)
usuario.retirar(200)
usuario.retirar(20000)

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto_uno = Point(5, 9)
punto_dos = Point(8, 5)
'''
# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def pago(self):
        print(f"{self.name} hoy has ganado {self.hourly_wage * self.hours_worked:.2f} Euros.")

empleado = Employee("Joseito", 12.31, 51)
empleado.pago()

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.
class Store:
    def __init__(self, inventory):
        pass

