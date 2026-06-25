# [SWAPPRITE] 🎨👾

Una herramienta ligera y rápida (CLI/GUI) para desarrolladores indie y artistas técnicos. Permite reemplazar la paleta de colores de un sprite indexado utilizando el cálculo de distancia visual en el espacio de color **CIELAB**, garantizando el mapeo de color más preciso posible para el ojo humano.

Ideal para pipelines de desarrollo retro, demakes, y ports a consolas clásicas (Sega Megadrive / Genesis, integración con SGDK, SNES, etc.), automatizando la adaptación de assets modernos a restricciones de hardware.

## ✨ Características

* **Precisión CIELAB:** No usa simples restas RGB. Convierte los colores al espacio LAB para entender qué color *parece* más cercano visualmente.
* **Respeto por el Índice 0:** El primer color de la paleta (índice `0`) se mantiene estrictamente como transparente, ideal para hardware retro.
* **Soporte GPL:** Lee nativamente archivos de paletas de GIMP / Aseprite (`.gpl`).
* **Doble Interfaz:** Usalo desde la terminal para procesamiento en lote (batch) o abrí la interfaz gráfica (GUI) para un uso rápido.
* **Mantiene el formato Indexado:** El PNG resultante sigue siendo Modo `P`, listo para ser inyectado en tu motor de juegos sin conversiones extra.

## 🚀 Instalación

1. Cloná este repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)
   cd nombre-del-repo

2. Instala las dependencias
    ```bash
    pip install Pillow

3. 💻 Uso  
    Interfaz Gráfica (GUI)
    Simplemente ejecutá el archivo de interfaz:
    ```bash 
    python interfaz.py

Línea de Comandos (CLI)
Para integrar en tus scripts de automatización:
    ```bash
    python main.py <imagen_original.png> <nueva_paleta.gpl> <imagen_salida.png>

🛠️ Próximas Características (Roadmap)
[ ] Soporte para redimensionado (Downscaling) con filtro Nearest Neighbor.

[ ] Armado automático de Spritesheets a partir de secuencias de imágenes.

[ ] Algoritmo de Dithering (Floyd-Steinberg) para paletas extremadamente limitadas.

📄 Licencia
Este proyecto está bajo la Licencia MIT - Siéntete libre de usarlo, modificarlo y compartirlo.

Copyright (c) 2026 Gustavo Enrique Valenzuela

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo.

