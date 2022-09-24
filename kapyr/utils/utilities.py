def get_image_extension(path):
    return path.split('.')[-1]

def get_image_name(path):
    name_with_extension = path.split('/')[-1]
    image_name = name_with_extension.split('.')[0]
    return image_name
