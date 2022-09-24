import rasterio
import numpy as np

from kapyr.utils.open import open_image
from kapyr.utils.utilities import get_image_extension, get_image_name

def compress_image(path):
    image_name = get_image_name(path=path) 
    image_extension = get_image_extension(path = path)

    image = open_image(path=path)
    image_numerical_data = image.read()
    tmp_path_image = '/tmp/' + image_name + 'compress' + '.' + image_extension

    normalized_image = (image_numerical_data * (255/np.max(image_numerical_data))).astype(np.uint16)

    with rasterio.open(
        tmp_path_image, 'w',
        driver = 'GTiff',
        nodata = 0,
        width = image.width,
        height = image.height,
        count = 3,
        dtype = normalized_image.dtype,
        crs = image.crs,
        transform = image.transform,
        compress = "LWZ",
    ) as new_image: new_image.write(image_numerical_data)

    return tmp_path_image