import sys
from PIL import Image
from color_utils import rgb_a_lab, calcular_distancia_lab
from parser_utils import leer_paleta_gpl

def procesar_sprite(ruta_img_original, ruta_paleta_nueva, ruta_img_salida):
    """
    Motor principal que toma una imagen indexada y le aplica una nueva paleta
    buscando los colores más cercanos matemáticamente (CIELAB).
    """
    # 1. Cargar nueva paleta
    paleta_nueva_rgb = leer_paleta_gpl(ruta_paleta_nueva)
    paleta_nueva_lab = [rgb_a_lab(*color) for color in paleta_nueva_rgb]

    # 2. Cargar imagen original
    img = Image.open(ruta_img_original)
    if img.mode != 'P':
        raise ValueError("La imagen original no está en modo indexado (P).")

    # 3. Extraer paleta original (Dinámico para evitar IndexError)
    paleta_plana = img.getpalette()
    paleta_original_rgb = []
    
    for i in range(0, len(paleta_plana), 3):
        if i + 2 < len(paleta_plana):
            paleta_original_rgb.append((paleta_plana[i], paleta_plana[i+1], paleta_plana[i+2]))

    # 4. Analizar cercanía de colores (CIELAB)
    mapa_indices = {}
    mapa_indices[0] = 0  # Protegemos el índice transparente
    
    colores_usados = max(img.getdata()) 
    
    for i in range(1, colores_usados + 1):
        # Si la imagen usa un índice que no está en la paleta original, lo salteamos
        if i >= len(paleta_original_rgb):
            continue
            
        color_orig = paleta_original_rgb[i]
        lab_orig = rgb_a_lab(*color_orig)
        
        distancia_minima = float('inf')
        mejor_indice = 0
        
        for j in range(1, len(paleta_nueva_lab)):
            dist = calcular_distancia_lab(lab_orig, paleta_nueva_lab[j])
            if dist < distancia_minima:
                distancia_minima = dist
                mejor_indice = j
                
        mapa_indices[i] = mejor_indice

    # 5. Re-indexar los píxeles
    datos_pixeles = list(img.getdata())
    nuevos_datos = [mapa_indices.get(pixel, 0) for pixel in datos_pixeles]

    nueva_img = Image.new('P', img.size)
    nueva_img.putdata(nuevos_datos)

    # 6. Inyectar paleta nueva
    paleta_nueva_plana = []
    for r, g, b in paleta_nueva_rgb:
        paleta_nueva_plana.extend([r, g, b])
        
    nueva_img.putpalette(paleta_nueva_plana)
    nueva_img.putpalette(paleta_nueva_plana)

    # 7. Guardar resultado
    nueva_img.save(ruta_img_salida, transparency=0)


# --- Soporte para uso por Consola / Terminal ---
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso por consola: python main.py <img_original.png> <paleta.gpl> <img_salida.png>")
        sys.exit(1)

    r_img = sys.argv[1]
    r_paleta = sys.argv[2]
    r_salida = sys.argv[3]

    print("Procesando...")
    try:
        procesar_sprite(r_img, r_paleta, r_salida)
        print(f"¡Éxito! Guardado en: {r_salida}")
    except Exception as e:
        print(f"Error: {e}")