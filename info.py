import pygame
from pygame.locals import *

        # self.liblaryCards = 20
        # self.graveyardCards = 0

class GameInfo(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, size, font_size, fontName):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(*pos, *size)
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)
        self.image = self.original_image.copy()
        self.font = pygame.font.SysFont(fontName, font_size)
        self.update()

    def update(self):
        self.text_surface = self.font.render(self.text(), True, (255, 255, 255))
        text_surface_size = self.text_surface.get_size()
        text_surface_center = (text_surface_size[0] // 2, text_surface_size[1] // 2)
        image_center = (self.rect.width // 2, self.rect.height // 2)
        blit_position = (image_center[0] - text_surface_center[0], image_center[1] - text_surface_center[1])
        self.image = self.original_image.copy()
        self.image.blit(self.text_surface, blit_position)
    

class Life(GameInfo):
    def __init__(self, life):
        self.life = life
        self.imgpath = "img/life.png"
        self.pos = (300,420)    #位置x,y
        self.size = (180,60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName)
    def text(self):
        return f"{self.life}"

class Mana(GameInfo):
    def __init__(self, mana):
        self.manaMax = mana
        self.manaCurrent = 1
        self.imgpath = "img/mana_blue.png"
        self.pos = (10, 420)    #位置x,y
        self.size = (180, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName)
    def text(self):
        return f"{self.manaCurrent} / {self.manaMax}"

class Library(GameInfo):
    def __init__(self, library):
        self.library = library
        self.imgpath = "img/library.png"
        self.pos = (10, 500)    #位置x,y
        self.size = (120, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName)
    def text(self):
        return f"{self.library}"
    
class Graveyard(GameInfo):
    def __init__(self, graveyard):
        self.graveyard = graveyard
        self.imgpath = "img/graveyard.png"
        self.pos = (10, 570)    #位置x,y
        self.size = (120, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName)
    def text(self):
        return f"{self.graveyard}"
    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgpath = "img/player.jpg"
        self.pos = (250, 140)    #位置x,y
        self.size = (280, 280)   #サイズw,h
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.image.load(self.imgpath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgpath = "img/enemy1.png"
        self.pos = (750, 140)    #位置x,y
        self.size = (280, 280)   #サイズw,h
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.image.load(self.imgpath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

class EnemyLife(GameInfo):
    def __init__(self, life):
        self.life = life
        self.imgpath = "img/life.png"
        self.pos = (800,420)    #位置x,y
        self.size = (180,60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName)
    def text(self):
        return f"{self.life}"
