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
        self._speed = 0

    def accelerate(self):
        self._speed += 10
    def brake(self):
        self._speed -= 10

# 4. Añade a la clase "Car" un método llamado "accelerate" que aumente la velocidad en 10 unidades. Añade también un método "brake" que reduzca la velocidad en 10 unidades. Asegúrate de que la velocidad no sea negativa.
coche = Car("BMW", "Z4")
coche.accelerate()
print(f"El {coche.brand} {coche.model} va a {coche._speed}km/H.")


# 5. Crea una clase "Book" que tenga propiedades como "title" (público) y "author" (privado). Añade un método para obtener el autor y otro para cambiar el título del libro.

# 6. Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas. Añade un método para calcular y devolver la nota media del estudiante.

# 7. Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta.

# 8. Crea una clase "Point" que represente un punto en el espacio 2D con coordenadas "x" e "y". Añade un método que calcule la distancia entre dos puntos.

# 9. Crea una clase "Employee" que tenga propiedades como "name", "hourly_wage" (pago por hora) y "hours_worked". Añade un método que calcule el pago total basado en las horas trabajadas y el salario por hora.

# 10. Crea una clase "Store" que tenga una propiedad "inventory" (una lista de productos). Añade un método para agregar un producto al inventario y otro para mostrar todos los productos disponibles.


