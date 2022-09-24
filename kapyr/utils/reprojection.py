import rasterio

from rasterio.warp import calculate_default_transform, reproject, Resampling
from kapyr.utils.utilities import get_image_name
from kapyr.utils.open import open_image


def change_image_projection(path, new_projection):
    image_name = '/tmp/' + get_image_name(path) 

    with rasterio.open(path, num_threads='8') as image:
        transform, width, height = calculate_default_transform(
            image.crs, new_projection, image.width, image.height, *image.bounds
        )
        kwargs = image.meta.copy()
        kwargs.update({
            'driver': 'GTiff',
            'crs': new_projection,
            'transform': transform,
            'width': width,
            'height': height,
        })

        with rasterio.open(image_name, 'w', **kwargs) as image_reprojected:
            for i in range(1, image.count + 1):
                reproject(
                    source = rasterio.band(image, i),
                    destination = rasterio.band(image_reprojected, i),
                    src_transform = image.transform,
                    src_crs = image.crs,
                    dst_transform = transform,
                    dst_crs = new_projection,
                    resampling = Resampling.nearest
                )
    
    return open_image(image_name)