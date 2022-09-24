# Función de transformación *move_image_coordinates_randomly*

Recibe una imagen con información geográfica y retorna la misma imagen cambiando su posición en el sistema de referencia por coordenadas.

## Funcionamienito

Se realiza la lectura de la información raster empleando la función open de rasterio, posteriormente se escribe una copia de la imagen con la misma metadata y el mismo array 
numérico, pero implementando el parámetro **compress** usando el método **Deflate**, éste último es un algoritmo Lossless que brinda una reducción del tamaño (en memoria)
de aproximadamente 1:10. La función retorna una imagen con el mismo formato de entrada. 

## Parámetros
- path: Ruta de la imagen de origen en formato tif, jp2 o img.

## Salidas
- path: Ruta de la imagen procesada en el mismo formato que la de origen. 

## Ejemplo 
```
from Kapyr.transform.move import move_image_coordinates_randomly

move_image_coordinates_randomly(path)
```
