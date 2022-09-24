# Función de compresión y reducción *resize_image*

Esta función realiza la compresión de una imagen en formato **ti**, **jp2** o **img**. Dicha compresión reduce la dimensión original de la imagen en un 95%. 


## Funcionamiento

En primera instancia se lee la imagen de tipo raster mediante la función open de rasterio, posteriormente, se separa el arreglo numérico de la metadata y se 
redimensiona adecuadamente con el fin de seguir el formato apto para OpenCV. Luego, se utiliza la función resize de OpenCv que disminuye la dimensión de cada 
una de las capas mediante el método de interpolación **INTER_CUBIC**. Con el nuevo arreglo numérico, se construye un archivo de tipo tif (j2 o img) cuya metada es igual a la original.

## Parámetros
- **path**: Ruta de la imagen de origen en formato tif, jp2 o img.

## Salidas
Retorna un string que incluye el path a la imagen procesada. Esta ruta se guarda en /temp

## Ejemplo
```
from kapyr.compres.lossy import resize_image
resize_image(path)
```
