# Librería **Kapyr**  1.01

En la primera versión de esta librería se implementan tres funciones principales:

- *move_image_coordinates_randomly:* Recibe una imagen con información geográfica y retorna la misma imagen cambiando su posición en el sistema de referencia por coordenadas.

- *resize_image:* Esta función realiza la compresión de una imagen en formato ti, jp2 o img. Dicha compresión reduce la dimensión original de la imagen en un 95%.

- *move_image_coordinates_randomly:* Recibe una imagen con información geográfica y retorna la misma imagen cambiando su posición en el sistema de referencia por coordenadas.

### Arquitectura

La arquitectura empleada en esta librería es la siguiente

kapyr/
  - utils/
    - open.py
    - export.py
    - reprojection.py
    - utilities.py
  - compress/
    - [lossy.py](https://github.com/anibarrao/kapyr/blob/feature/add-documentation/doc/compress/lossy.md)
    - [lossless.py](https://github.com/anibarrao/kapyr/blob/feature/add-documentation/doc/compress/lossless.md)
  - transform/
    - [move.py](https://github.com/anibarrao/kapyr/blob/feature/add-documentation/doc/transform/move.md)

En donde las funciones principales se encuentran en move, lossy y lossles, respectivamente. Éstas se alimentan de funciones más sencillas que se encuentran en la carpeta utils.
Siguiendo de esta manera una arquitectura típica de de una librería de Python. Cabe recordar que todas las funciones principales retornan imágenes en el mismo formato que la
imagen de entrada.
