import tkinter as tk
from tkinter import filedialog, messagebox
from main import procesar_sprite 

def seleccionar_imagen():
    ruta = filedialog.askopenfilename(
        title="Seleccionar Sprite Original",
        filetypes=[("Imágenes PNG", "*.png"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        lbl_img_path.config(text=ruta)
        btn_procesar.config(state="normal" if verificar_listo() else "disabled")

def seleccionar_paleta():
    ruta = filedialog.askopenfilename(
        title="Seleccionar Paleta Nueva",
        filetypes=[("Paletas GIMP/Aseprite", "*.gpl"), ("Todos los archivos", "*.*")]
    )
    if ruta:
        lbl_paleta_path.config(text=ruta)
        btn_procesar.config(state="normal" if verificar_listo() else "disabled")

def verificar_listo():
    # Chequea que ambas rutas estén cargadas antes de habilitar el botón de procesar
    return lbl_img_path.cget("text") != "Ninguna imagen seleccionada" and \
           lbl_paleta_path.cget("text") != "Ninguna paleta seleccionada"

def ejecutar_proceso():
    ruta_img = lbl_img_path.cget("text")
    ruta_paleta = lbl_paleta_path.cget("text")
    usar_dither = var_dithering.get() # Capturamos si el usuario tildó la opción
    
    # Pedimos al usuario dónde quiere guardar el resultado
    ruta_salida = filedialog.asksaveasfilename(
        title="Guardar resultado como...",
        defaultextension=".png",
        filetypes=[("Imágenes PNG", "*.png")]
    )
    
    if not ruta_salida:
        return # El usuario canceló el guardado

    try:
        # Llamamos a tu motor de reemplazo de paletas pasándole la opción de dithering
        procesar_sprite(ruta_img, ruta_paleta, ruta_salida, usar_dithering=usar_dither)
        messagebox.showinfo("¡Éxito!", "El sprite fue re-colorizado y guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema al procesar:\n{e}")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Swapprite - Retro Dev Tool")
ventana.geometry("500x320") # Agrandamos un poquito el alto para que entre el checkbox
ventana.resizable(False, False)
ventana.config(padx=20, pady=20)

# Título
tk.Label(ventana, text="Reemplazo de Paleta (CIELAB)", font=("Arial", 14, "bold")).pack(pady=(0, 15))

# Sección Imagen
marco_img = tk.LabelFrame(ventana, text="1. Sprite Original", padx=10, pady=5)
marco_img.pack(fill="x", pady=5)
btn_img = tk.Button(marco_img, text="Buscar PNG", command=seleccionar_imagen)
btn_img.pack(side="left")
lbl_img_path = tk.Label(marco_img, text="Ninguna imagen seleccionada", fg="gray", wraplength=350)
lbl_img_path.pack(side="left", padx=10)

# Sección Paleta
marco_paleta = tk.LabelFrame(ventana, text="2. Paleta de Destino", padx=10, pady=5)
marco_paleta.pack(fill="x", pady=5)
btn_paleta = tk.Button(marco_paleta, text="Buscar .GPL", command=seleccionar_paleta)
btn_paleta.pack(side="left")
lbl_paleta_path = tk.Label(marco_paleta, text="Ninguna paleta seleccionada", fg="gray", wraplength=350)
lbl_paleta_path.pack(side="left", padx=10)

# --- Opción de Dithering ---
var_dithering = tk.BooleanVar(value=False) # Arranca desactivado por defecto
chk_dither = tk.Checkbutton(ventana, text="Aplicar Dithering (Floyd-Steinberg)", variable=var_dithering, font=("Arial", 10))
chk_dither.pack(pady=5)

# Botón Procesar (Inicia deshabilitado)
btn_procesar = tk.Button(ventana, text="🔄 PROCESAR Y GUARDAR", font=("Arial", 12, "bold"), 
                        bg="#4CAF50", fg="white", state="disabled", command=ejecutar_proceso, pady=10)
btn_procesar.pack(side="bottom", fill="x", pady=10)

ventana.mainloop()