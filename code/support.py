from settings import * 

def import_images(*path, format = 'png', is_alpha = True):
    full_path = join(*path) + f'.{format}'
    loaded_image = pygame.image.load(full_path)
    surf = loaded_image.convert_alpha() if is_alpha else loaded_image.conver()
    return surf

def import_folder(*path):
    frames = []
    for folder_path, sub_folder, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surf = pygame.image.load(full_path).convert_alpha()
            frames.append(surf)
    return frames