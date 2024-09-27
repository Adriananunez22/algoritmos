import tkinter as tk
import random
from tkinter import messagebox
from tkinter import simpledialog


# Función para comenzar un nuevo juego con la categoría seleccionada
def nuevo_juego(categoria):
    global puntaje, nivel, categoria_juego
    puntaje = 0
    nivel = 1
    categoria_juego = categoria
    lbl_puntaje.config(text=f"Puntaje: {puntaje}")
    lbl_nivel.config(text=f"Nivel: {nivel}")

    # Generar el primer reto dependiendo de la categoría seleccionada
    if categoria_juego == "Matemáticas":
        generar_reto_matematicas()
    elif categoria_juego == "Adivinanza":
        generar_reto_adivinanza()
    elif categoria_juego == "Habilidad":
        generar_reto_habilidad()


# Función para mostrar las instrucciones del juego
def mostrar_instrucciones():
    instrucciones = """
    Instrucciones:
    1. Selecciona una categoría para comenzar.
    2. Cada nivel presenta un reto diferente.
    3. Resuelve los retos para ganar puntos y avanzar niveles.
    4. Las categorías disponibles son:
       - Adivinanza
       - Matemáticas
       - Habilidad
    """
    lbl_instrucciones.config(text=instrucciones)


# Función para un desafío matemático (resolviendo una operación básica)
def juego_matematicas(opcion):
    global respuesta_correcta
    if opcion == respuesta_correcta:
        incrementar_puntaje()
        lbl_resultado.config(text="¡Correcto!")
        generar_reto_matematicas()  # Generar un nuevo reto automáticamente al acertar
    else:
        mostrar_puntaje_final()


# Función para generar un nuevo desafío matemático
def generar_reto_matematicas():
    global respuesta_correcta
    operacion = random.choice(['+', '-', '*'])
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    respuesta_correcta = eval(f"{num1} {operacion} {num2}")
    lbl_desafio.config(text=f"¿Cuánto es {num1} {operacion} {num2}?")

    # Crear botones de opciones de respuesta
    opciones = [respuesta_correcta, random.randint(1, 100), random.randint(1, 100)]
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        botones_respuesta[i].config(text=str(opcion), command=lambda x=opcion: juego_matematicas(x))


# Función para generar un reto de adivinanza (simple adivinanza de número)
def generar_reto_adivinanza():
    global respuesta_correcta
    respuesta_correcta = random.randint(1, 10)
    lbl_desafio.config(text="Adivina el número entre 1 y 10:")

    # Crear botones de opciones de respuesta
    opciones = [respuesta_correcta, random.randint(1, 10), random.randint(1, 10)]
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        botones_respuesta[i].config(text=str(opcion), command=lambda x=opcion: juego_adivinanza(x))


def juego_adivinanza(opcion):
    global respuesta_correcta
    if opcion == respuesta_correcta:
        incrementar_puntaje()
        lbl_resultado.config(text="¡Correcto!")
        generar_reto_adivinanza()
    else:
        mostrar_puntaje_final()


# Función para generar un reto de habilidad (reacción rápida)
def generar_reto_habilidad():
    global respuesta_correcta
    respuesta_correcta = random.randint(1, 3)  # Simular un reto simple de habilidad
    lbl_desafio.config(text="Elige el número correcto rápidamente:")

    # Crear botones de opciones de respuesta
    opciones = [respuesta_correcta, random.randint(1, 3), random.randint(1, 3)]
    random.shuffle(opciones)
    for i, opcion in enumerate(opciones):
        botones_respuesta[i].config(text=str(opcion), command=lambda x=opcion: juego_habilidad(x))


def juego_habilidad(opcion):
    global respuesta_correcta
    if opcion == respuesta_correcta:
        incrementar_puntaje()
        lbl_resultado.config(text="¡Correcto!")
        generar_reto_habilidad()
    else:
        mostrar_puntaje_final()


# Función para incrementar puntaje y avanzar nivel
def incrementar_puntaje():
    global puntaje, nivel
    puntaje += 10
    nivel += 1
    lbl_puntaje.config(text=f"Puntaje: {puntaje}")
    lbl_nivel.config(text=f"Nivel: {nivel}")


# Función para mostrar el puntaje final y preguntar si se desea continuar o salir
def mostrar_puntaje_final():
    messagebox.showinfo("Juego terminado", f"Puntaje total: {puntaje}")
    respuesta = messagebox.askquestion("Continuar o salir", "¿Quieres continuar jugando?")

    if respuesta == 'yes':
        nuevo_juego(categoria_juego)
    else:
        ventana.quit()


# Función para salir del juego manualmente
def salir_del_juego():
    respuesta = messagebox.askyesno("Salir", "¿Estás seguro de que deseas salir?")
    if respuesta:
        ventana.quit()


# Función para pedir el nombre del jugador al inicio
def pedir_nombre_jugador():
    nombre = simpledialog.askstring("Nombre del jugador", "Por favor, introduce tu nombre:")
    if nombre:
        return nombre
    else:
        messagebox.showwarning("Nombre necesario", "Debes ingresar un nombre para continuar.")
        return pedir_nombre_jugador()


# Diseño de la interfaz gráfica usando Tkinter
ventana = tk.Tk()
ventana.title("Juego de Estrategia, Matemáticas y Habilidad")
ventana.geometry("400x600")

# Pedir el nombre del jugador al iniciar
nombre_jugador = pedir_nombre_jugador()

puntaje = 0
nivel = 1
categoria_juego = ""

# Sección de información y botones
frame_info = tk.Frame(ventana, bg="#f0f0f0", bd=5)
frame_info.pack(fill="x")

lbl_puntaje = tk.Label(frame_info, text=f"Puntaje: {puntaje}", font=("Arial", 14), bg="#f0f0f0")
lbl_puntaje.grid(row=0, column=0, padx=10)

lbl_nivel = tk.Label(frame_info, text=f"Nivel: {nivel}", font=("Arial", 14), bg="#f0f0f0")
lbl_nivel.grid(row=0, column=1, padx=10)

btn_instrucciones = tk.Button(ventana, text="Instrucciones", command=mostrar_instrucciones, bg="#87ceeb",
                              font=("Arial", 12))
btn_instrucciones.pack(pady=10)

lbl_instrucciones = tk.Label(ventana, text="", wraplength=300, bg="#fafafa", font=("Arial", 10))
lbl_instrucciones.pack(pady=10)

# Selección de categoría
lbl_categoria = tk.Label(ventana, text="Selecciona una categoría:", font=("Arial", 14), bg="#fafafa")
lbl_categoria.pack(pady=10)

btn_matematicas = tk.Button(ventana, text="Matemáticas", command=lambda: nuevo_juego("Matemáticas"), bg="#90ee90",
                            font=("Arial", 12))
btn_matematicas.pack(pady=5)

btn_adivinanza = tk.Button(ventana, text="Adivinanza", command=lambda: nuevo_juego("Adivinanza"), bg="#90ee90",
                           font=("Arial", 12))
btn_adivinanza.pack(pady=5)

btn_habilidad = tk.Button(ventana, text="Habilidad", command=lambda: nuevo_juego("Habilidad"), bg="#90ee90",
                          font=("Arial", 12))
btn_habilidad.pack(pady=5)

# Desafío dinámico
lbl_desafio = tk.Label(ventana, text="", font=("Arial", 14), bg="#fafafa")
lbl_desafio.pack(pady=10)

# Crear botones para las respuestas
botones_respuesta = []
for i in range(3):
    btn = tk.Button(ventana, text="", width=10, bg="#90ee90", font=("Arial", 12))
    btn.pack(pady=5)
    botones_respuesta.append(btn)

# Botón para salir del juego
btn_salir = tk.Button(ventana, text="Salir del Juego", command=salir_del_juego, bg="#ff6347", font=("Arial", 12))
btn_salir.pack(pady=10)

# Resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12), bg="#fafafa")
lbl_resultado.pack(pady=10)

ventana.mainloop()
