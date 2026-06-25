def leer_paleta_gpl(ruta_archivo):
    """
    Lee un archivo .gpl (GIMP Palette) y devuelve una lista de tuplas (R, G, B).
    Mantiene estrictamente el orden del archivo, asegurando que la primera línea
    de color sea el índice 0 (transparente).
    """
    colores = []
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        
    # Verificar que sea un archivo GPL válido
    if not lineas or "GIMP Palette" not in lineas[0]:
        raise ValueError("El archivo no parece ser una paleta de GIMP (.gpl) válida.")
        
    for linea in lineas:
        linea = linea.strip()
        
        # Saltamos líneas vacías, comentarios o la cabecera de metadatos
        if not linea or linea.startswith('#') or linea.startswith('GIMP Palette') or linea.startswith('Name:') or linea.startswith('Columns:'):
            continue
            
        try:
            # Los archivos GPL separan los valores por espacios o tabulaciones.
            # split() sin argumentos limpia cualquier cantidad de espacios en blanco.
            partes = linea.split()
            
            # Los primeros 3 elementos sí o sí tienen que ser R, G y B
            r = int(partes[0])
            g = int(partes[1])
            b = int(partes[2])
            
            # Validación rápida de rango de color
            if all(0 <= c <= 255 for c in (r, g, b)):
                colores.append((r, g, b))
        except (ValueError, IndexError):
            # Si una línea falla al parsear (por ejemplo texto extraño), la salteamos
            continue
            
    if not colores:
        raise ValueError("No se encontraron colores válidos en el archivo .gpl.")
        
    return colores