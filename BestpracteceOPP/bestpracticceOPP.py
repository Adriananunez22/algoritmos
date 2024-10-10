class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre


# Función para capturar datos de 3 alumnos desde teclado
def capturar_alumnos():
    alumnos = []

    for i in range(3):
        print(f"\nCaptura de datos para el alumno {i + 1}")
        nombre = input("Nombre: ")
        apellido_paterno = input("Apellido Paterno: ")
        apellido_materno = input("Apellido Materno: ")
        no_control = input("Número de Control: ")
        semestre = input("Semestre: ")

        # Crear un objeto Alumno con los datos capturados
        alumno = Alumno(nombre, apellido_paterno, apellido_materno, no_control, semestre)

        # Agregar el objeto Alumno a la lista
        alumnos.append(alumno)

    return alumnos


# Función para mostrar los registros de los alumnos
def mostrar_alumnos(alumnos):
    for i, alumno in enumerate(alumnos, 1):
        print(f"\nDatos del alumno {i}:")
        print(f"Nombre: {alumno.get_nombre()}")
        print(f"Apellido Paterno: {alumno.get_apellido_paterno()}")
        print(f"Apellido Materno: {alumno.get_apellido_materno()}")
        print(f"Número de Control: {alumno.get_no_control()}")
        print(f"Semestre: {alumno.get_semestre()}")


# Ejecución principal
alumnos = capturar_alumnos()
mostrar_alumnos(alumnos)
