from kapyr.compress.lossless import compress_image
from kapyr.compress.lossy import resize_image
from kapyr.transform.move import move_image_coordinates_randomly
from kapyr.utils.export import save_image

def process_image(path):
    img_moved = move_image_coordinates_randomly(path)
    img_compressed_lossless = compress_image(path)
    print(img_moved, img_compressed_lossless)

if __name__ == "__main__":
    path_to_image = './nepal_lc_2020.tiff'
    process_image(path=path_to_image)