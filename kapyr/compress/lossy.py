import numpy as np
import cv2

from kapyr.utils.open import open_image
from kapyr.utils.export import save_image
from kapyr.utils.utilities import get_image_extension, get_image_name


def resize_image(path):
    image_name = get_image_name(path= path)
    extension_image = get_image_extension(path=path)
    tmp_image_path = '/tmp/' + image_name + extension_image
    image = open_image(path = path)
    image_numerical_data = image.read()

    image_nomarlized = (image_numerical_data * (255 / np.max(image_numerical_data))).astype(np.uint8)
    normalized_image_ordered = np.moveaxis(image_nomarlized, [0,1,2], [2,0,1])
    small_image = cv2.resize(
        normalized_image_ordered, 
        (int(normalized_image_ordered.shape[1]*np.sqrt(0.05)), (int(normalized_image_ordered.shape[0]*np.sqrt(0.05)))),
        interpolation = cv2.INTER_CUBIC,
    )

    image_to_export = np.moveaxis(small_image, [0,1,2], [1,2,0])

    path_to_image = save_image(
        path = tmp_image_path,
        function = 'resize',
        height = image_to_export.shape[1],
        width = image_to_export.shape[2],
        count = image_to_export.count[0],
        dtype = image_to_export.dtype,
        crs = image.crs,
        transform = image.transform,
        image = image_nomarlized,
    )

    return path_to_image