class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad, altura, peso, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.nacionalidad = nacionalidad


    # Método 1: Mostrar los detalles de la persona
    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Altura: {self.altura} metros")
        print(f"Peso: {self.peso} kg")
        print(f"Nacionalidad: {self.nacionalidad}")

    # Método 2: Calcular el índice de masa corporal (IMC)
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return f"El IMC de {self.nombre} es: {imc:.2f}"

    # Método 3: Verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad."
        else:
            return f"{self.nombre} es menor de edad."

    # Método 4: Actualizar la edad
    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad
        print(f"La edad de {self.nombre} se ha actualizado a {self.edad} años.")

    # Método 5: Cambiar la nacionalidad
    def cambiar_nacionalidad(self, nueva_nacionalidad):
        self.nacionalidad = nueva_nacionalidad
        print(f"{self.nombre} ahora tiene la nacionalidad {self.nacionalidad}.")

# Crear una instancia (objeto) de la clase Persona
persona1 = Persona("juan", 22, 1.55, 15, "Mexicana")
persona2 = Persona("adriana", 21, 1.58, 80, "francesa")
persona3 = Persona("eduardo", 24, 1.80, 90, "alemana")

# Usar los métodos de la instancia
persona1.mostrar_detalles()                 # Mostrar los detalles de la persona
print(persona1.calcular_imc())              # Calcular el IMC
print(persona1.es_mayor_de_edad())          # Verificar si es mayor de edad
persona1.actualizar_edad(30)                # Actualizar la edad
persona1.cambiar_nacionalidad("Canadiense") # Cambiar la nacionalidad

persona2.mostrar_detalles()                 # Mostrar los detalles de la persona
print(persona2.calcular_imc())              # Calcular el IMC
print(persona2.es_mayor_de_edad())          # Verificar si es mayor de edad
persona2.actualizar_edad(30)                # Actualizar la edad
persona2.cambiar_nacionalidad("Canadiense") # Cambiar la nacionalidad

persona3.mostrar_detalles()                 # Mostrar los detalles de la persona
print(persona3.calcular_imc())              # Calcular el IMC
print(persona3.es_mayor_de_edad())          # Verificar si es mayor de edad
persona3.actualizar_edad(30)                # Actualizar la edad
persona3.cambiar_nacionalidad("Canadiense") # Cambiar la nacionalidad
