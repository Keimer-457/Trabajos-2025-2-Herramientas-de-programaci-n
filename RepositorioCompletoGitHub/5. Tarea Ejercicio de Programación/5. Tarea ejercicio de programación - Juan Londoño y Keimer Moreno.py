# -----------------------------------------------------
# Trabajo en Python - Interfaz Gráfica (Tkinter)
# Presentado por (GRUPO): Juan Sebastian Londoño: 1065871157   y   Keimer Duvan Moreno: 1077436457
# para no hacer el codigo extenso y repetitivo con una funcion independiente para cada uno, use lambda
# -----------------------------------------------------

import tkinter as tk
from tkinter import messagebox, PhotoImage

# ---------- FUNCIÓN 1: Mostrar mensaje + FUNCION PARA formulario.txt----------

import webbrowser
import tkinter as tk

def mostrar_mensaje():
    """Muestra un mensaje de bienvenida con un botón clickeable que abre el formulario en el navegador."""
    ventana_msg = tk.Toplevel(ventana)
    ventana_msg.title("Mensaje")
    ventana_msg.geometry("300x125")
    ventana_msg.resizable(False, False)
    ventana_msg.grab_set()  # Hace modal la ventana

    # mensaje
    etiqueta = tk.Label(ventana_msg, text="Bienvenido a nuestro programa GUI", font=("Arial", 12))
    etiqueta.pack(pady=20)

    # Enlace 
    link_formulario = "https://drive.google.com/file/d/1h2Pb7hTRITO1caLawjyfZu1SKOn3Nc4R/preview"

    def abrir_formulario():
        webbrowser.open(link_formulario)  # Abre el enlace en el navegador predeterminado
        ventana_msg.destroy()  # Cierra la ventana del mensaje

    # configuracion
    boton_link = tk.Button(ventana_msg, text="formulario.txt", font=("Arial", 10, "underline"),
                           fg="blue", cursor="hand2", bd=0, command=abrir_formulario)
    boton_link.pack(pady=5)

# ---------- FUNCIÓN 2: Cambiar color de fondo ----------
def cambiar_color():
    """Cambia el color del fondo de la ventana principal."""
    colores = ["lightblue", "lightgreen", "lightyellow", "lavender", "pink"]
    color_actual = ventana.cget("bg")
    nuevo_color = colores[(colores.index(color_actual) + 1) % len(colores)] if color_actual in colores else colores[0] # cambio distintos colores
    ventana.configure(bg=nuevo_color)

# ---------- FUNCIÓN 3: Abrir nueva ventana ----------
def abrir_segunda_ventana():
    """Abre una nueva ventana secundaria con desplazamiento general."""
    nueva = tk.Toplevel(ventana)
    nueva.title("Ventana Secundaria")
    nueva.geometry("400x250")
    nueva.resizable(False, False)
    nueva.config(bg="lightgray")

    # --- Contenedor con canvas y el scroll es el marco Frame donde ira todo el contenido
    # --- para que se pueda scrollear
    contenedor = tk.Frame(nueva)
    contenedor.pack(fill="both", expand=True)

    # borde y para que se pueda expandir
    canvas = tk.Canvas(contenedor, bg="lightgray", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    
    # --- fijo en y para scrollear
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    # Hace que el scroll se actualice cuando mueves el canvas (sincroniza ambos).
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    frame_interno = tk.Frame(canvas, bg="lightgray")
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # --- Habilitar scroll con la rueda del mouse ---
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units") # separada en 120 unidades la barra de movilizaje 
    canvas.bind("<MouseWheel>", _on_mousewheel) # conectar que este moviendose y canva sea ctiva

    # --- CONTENIDO DE LA VENTANA ---
    etiqueta = tk.Label(frame_interno, text="Ventana secundaria con imagen y botón", bg="lightgray", font=("Arial", 12))
    etiqueta.pack(pady=15)


    # Imagen en base64
    # -- Convertimos la iamgen en base x64 porque pense como el archivo se envia .py pues
    #    no puede enviarse la imagen consigo asi que utilize esta idea

    imagen_base64 = """
    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
    """  

    try:
        img = PhotoImage(data=imagen_base64)
        lbl_img = tk.Label(frame_interno, image=img, bg="lightgray")
        lbl_img.image = img  # referencia paa evitar que se borre
        lbl_img.pack(pady=10)
    except:
        lbl_img = tk.Label(frame_interno, text="[Sin imagen cargada]", bg="lightgray")
        lbl_img.pack(pady=10)

    # personalizaje para la ventana 2
    btn_saludo = tk.Button(frame_interno, text="Saludo desde la ventana 2",
                           command=lambda: messagebox.showinfo("Saludo", "Hola, esta es la segunda ventana buen dia"))
    btn_saludo.pack(pady=10)

    tk.Label(frame_interno, text="", bg="lightgray", height=10).pack()

    # --- Mini título en cursiva ---
    # Pista
    mini_titulo = tk.Label(frame_interno, text="Escriba un comando   (pista: cerrar)", 
                       bg="lightgray", font=("Arial", 10, "italic"))
    mini_titulo.pack(pady=(10, 2))
    
    tk.Label(frame_interno, text="text", bg="lightgray").pack(pady=(10, 5))
    cuadro_coords = tk.Text(frame_interno, height=4, width=30, font=("Courier", 9))
    cuadro_coords.pack(pady=(0, 20))

# -- Función para el comando cerrar 
    def ejecutar_comando(event=None):
        comando = cuadro_coords.get("1.0", "end").strip().lower() # - Permite mayuscula y minuscula
        if comando == "cerrar":
            ventana.destroy()  # cierra toda la aplicación
        else:
            messagebox.showinfo("Comando no reconocido", f"'{comando}' no es un comando válido")

    cuadro_coords.bind("<Return>", lambda event: ejecutar_comando()) # de nuevo lambda para no def - inir

# ---------- INTERFAZ PRINCIPAL ----------
def interfaz_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Interfaz Principal - Tkinter")
    ventana.geometry("500x400")
    ventana.configure(bg="lightblue")

    # --- Frame contenedor principal (horizontal) ---
    frame_principal = tk.Frame(ventana, bg="lightblue")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

    # --- Frame izquierdo: botones y título ---
    frame_izq = tk.Frame(frame_principal, bg="lightblue")
    frame_izq.pack(side="left", fill="both", expand=True)

    titulo = tk.Label(frame_izq, text="PROYECTO PYTHON - GUI", bg="lightblue", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)

    boton1 = tk.Button(frame_izq, text="Mostrar Mensaje", font=("Arial", 12), command=mostrar_mensaje)
    boton1.pack(pady=10)

    boton2 = tk.Button(frame_izq, text="Cambiar el Color del Fondo", font=("Arial", 12), command=cambiar_color)
    boton2.pack(pady=10)

    boton3 = tk.Button(frame_izq, text="Abrir Segunda Ventana", font=("Arial", 12), command=abrir_segunda_ventana)
    boton3.pack(pady=10)

    for boton in [boton1, boton2, boton3]:
        boton.bind("<Enter>", lambda e: e.widget.config(cursor="hand2"))
        boton.bind("<Leave>", lambda e: e.widget.config(cursor="arrow"))

    # --- Frame derecho: imagen ---
    frame_der = tk.Frame(frame_principal, bg="lightblue")
    frame_der.pack(side="right", fill="both", expand=True)


    imagen_base64 = """
    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
    """  

    try:
        img_derecha = PhotoImage(data=imagen_base64)
        lbl_img = tk.Label(frame_der, image=img_derecha, bg="lightblue")
        lbl_img.image = img_derecha
        lbl_img.pack(padx=10, pady=10)
    except:
        lbl_img = tk.Label(frame_der, text="[Sin imagen]", bg="lightblue")
        lbl_img.pack(padx=10, pady=10)

    # --- Pie de página ---
    pie = tk.Label(ventana, text="Hecho por el grupo JuanKeimer", bg="lightblue", font=("Arial", 10))
    pie.pack(side="bottom", pady=10)

    pie = tk.Label(ventana, text="HERRAMIENTAS PROGRAMACION", bg="lightblue", font=("ArialBlack", 40))
    pie.pack(side="bottom", pady=200)  


    ventana.mainloop()

# ---------- EJECUCIÓN PRINCIPAL ----------
if __name__ == "__main__":
    interfaz_principal()
