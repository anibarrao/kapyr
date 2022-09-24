import rasterio

import kapyr.utils.utilities as utils

def save_image(path, function, height, width, bands, dtype, crs, transform, image):
    """

    """
    image_extension = utils.get_image_extension(path)
    image_name = utils.get_image_name(path)
    tmp_file_name = image_name + '_' + function + '.' + image_extension

    with rasterio.open(
        tmp_file_name, 'w',
        driver = 'GTiff', 
        height = height,
        width = width,
        count = bands,
        crs = crs, 
        transform = transform,
        dtype = dtype,
    ) as image_to_save: image_to_save.write(image)

    return tmp_file_name

    


