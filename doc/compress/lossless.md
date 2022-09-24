# Función de compresión *compress_image*

Esta función comprime una imagen geoespacial de tipo raster mediante un método lossless sin pérdida de resolución

## Funcionamiento 
Este método consta de dos fases, en la primera se leen los datos mediante el comando open de rasterio, posteriormente, se eliminan las bandas diferentes a RGB y 
se normaliza a escala 0-255, finalmente se guarda la imagen mediante un el método de compresión LZW. La segunda fase consiste en realizar otra compresión mediante 
el método Deflate, que también es de tipo lossless.

## Parámetros
- **path**: Ruta de la imagen de origen en formato tif, jp2 o img.

## Salidas
Retorna un string que incluye el path a la imagen procesada. Esta ruta se guarda en /temp. El formato de la imágen de salida es el mismo de origen.

## Ejemplo
```
from kapyr.compres.lossless compress_image
compress_image(path)

