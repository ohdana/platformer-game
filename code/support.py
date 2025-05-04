from settings import * 

def import_images(*path, format = 'png', is_alpha = True):
    full_path = join(*path) + f'.{format}'
    loaded_image = pygame.image.load(full_path)
    surf = loaded_image.convert_alpha() if is_alpha else loaded_image.conver()
    return surf

def import_folder(*path):
    frames = []
    for folder_path, sub_folder, file_names in walk(join(*path)):
        for file_name in sorted(file_names, key = lambda name: int(name.split('.')[0])):
            full_path = join(folder_path, file_name)
            surf = pygame.image.load(full_path).convert_alpha()
            frames.append(surf)
    return frames

def audio_importer(*path):
    audio_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            audio_dict[file_name.split('.')[0]] = pygame.mixer.Sound(full_path)
            
    return audio_dict