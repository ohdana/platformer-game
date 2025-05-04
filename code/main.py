from settings import * 
from sprites import *
from groups import AllSprites
from support import *
from random import randint

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups 
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        
        # load game
        self.load_assets()
        self.setup()
        
        # timers
        self.bee_timer = Timer(500, func = self.create_bee, autostart = True, repeat = True)
        
    def create_bee(self):
        Bee(self.bee_frames, ((randint(300,600)),(randint(300,600))), self.all_sprites)
        
    def load_assets(self):
        self.player_frames = import_folder('images', 'player')
        self.bullet_surf = import_images('images', 'gun', 'bullet')
        self.fire_surf = import_images('images', 'gun', 'fire')
        self.bee_frames = import_folder('images', 'enemies', 'bee')
        self.worm_frames = import_folder('images', 'enemies', 'worm')

        self.audio = audio_importer('audio')
        
    def setup(self):
        tmx_map = load_pygame(join('data', 'maps', 'world.tmx'))
        for x, y, image in tmx_map.get_layer_by_name('Main').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, (self.all_sprites, self.collision_sprites))
        for x, y, image in tmx_map.get_layer_by_name('Decoration').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, (self.all_sprites))
        
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites, self.player_frames)
        
        Worm(self.worm_frames, (700, 600), self.all_sprites)
        
    def run(self):
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 
            
            # update
            self.bee_timer.update()
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(BG_COLOR)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run() 