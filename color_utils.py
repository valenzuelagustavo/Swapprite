import math

def rgb_a_lab(r, g, b):
    """
    Convierte un color RGB (0-255) al espacio de color CIELAB.
    """
    # 1. Normalizar los valores RGB a un rango de 0 a 1
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # 2. Convertir RGB a sRGB lineal (corrección gamma)
    def linearize(canal):
        if canal > 0.04045:
            return ((canal + 0.055) / 1.055) ** 2.4
        else:
            return canal / 12.92

    r = linearize(r) * 100.0
    g = linearize(g) * 100.0
    b = linearize(b) * 100.0

    # 3. Convertir sRGB a XYZ (usando el iluminante estándar D65)
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505

    # 4. Convertir XYZ a CIELAB
    # Normaliza contra los valores de referencia del iluminante D65
    x = x / 95.047
    y = y / 100.000
    z = z / 108.883

    def pivot(n):
        if n > 0.008856:
            return n ** (1.0 / 3.0)
        else:
            return (7.787 * n) + (16.0 / 116.0)

    x, y, z = pivot(x), pivot(y), pivot(z)

    # Cálculo final de las coordenadas L* a* b*
    l = (116 * y) - 16
    a = 500 * (x - y)
    b_val = 200 * (y - z) 

    return l, a, b_val

def calcular_distancia_lab(lab1, lab2):
    """
    Calcula la distancia euclidiana entre dos colores en el espacio CIELAB.
    Acá es donde ocurre la magia de la similitud visual.
    """
    dl = lab1[0] - lab2[0]
    da = lab1[1] - lab2[1]
    db = lab1[2] - lab2[2]
    
    return math.sqrt(dl**2 + da**2 + db**2)