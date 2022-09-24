import rasterio

from kapyr.utils.utilities import get_image_extension 

def open_image(path):
    image_extension = get_image_extension(path)

    if image_extension == 'jp2':
        image = rasterio.open(path)
        return image
    else: 
        image = rasterio.open(path, num_threads='8')
        return image