# Función de transformación *move_image_coordinates_randomly*

Recibe una imagen con información geográfica y retorna la misma imagen cambiando su posición en el sistema de referencia por coordenadas.

## Funcionamienito
Se realiza la lectura de la imagen empleando la función open de rasterio, conviertierndo el *crs* a estándar wgs24. Luego, se generan dos números aleatorios, uno entre -180 y 180 y el otro entre  -90 y 90, correspondientes a la posición x e y. Posteriormente, se define un transform.affine con las coordenadas cambiadas y se usa para crear una copia de la imagen original (misma metadata y arreglo numérico de imagen) pero con la transformación trasladada.   

## Parámetros
- path: Ruta de la imagen de origen en formato tif, jp2 o img.

## Salidas
- path: Ruta de la imagen procesada en el mismo formato que la de origen. 

## Ejemplo 
```
from Kapyr.transform.move import move_image_coordinates_randomly

move_image_coordinates_randomly(path)
```
