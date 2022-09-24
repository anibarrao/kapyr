import rasterio
import numpy as np

from kapyr.utils.reprojection import change_image_projection
from kapyr.utils.export import save_image

gps_projection = 'EPSG:4326'

def move_image_coordinates_randomly(path):
    image = change_image_projection(path, gps_projection)

    image_numerical_data = image.read()
    image_transform_parameters = image.transform
    x_coord = image_transform_parameters.c

    np.random.seed(abs(round(x_coord)))
    new_x_coordinate = np.random.randint(-180,180)
    new_y_coordinate = np.random.randint(-90,90)

    new_affine_transformation = rasterio.Affine(
        image_transform_parameters.a, 
        image_transform_parameters.b, 
        new_x_coordinate, 
        image_transform_parameters.d, 
        image_transform_parameters.e, 
        new_y_coordinate,
    )

    displaced_image_path = save_image(
        path = path,
        function = 'displacement',
        height = image.height,
        width = image.width,
        bands = image.count,
        dtype = image_numerical_data.dtype,
        crs = image.crs,
        transform = new_affine_transformation,
        image=image_numerical_data
    )

    return displaced_image_path