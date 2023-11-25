import pygame
from pygame.locals import *

class life(pygame.sprite.Sprite):
    def __init__(self,life):
        pygame.sprite.Sprite.__init__(self)
        self.life = life    #引数で貰った初期ライフ
        self.width = 200    #横幅
        self.height = 200   #縦幅
        self.x = 300
        self.y = 300
        self.rect = Rect(self.x, self.y, self.width, self.height) #画像のx,y軸とサイズ
        self.original_image = pygame.image.load("img/life.png").convert_alpha()  # 画像を一度だけロード
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))  # 画像サイズをsurfaceのサイズに修正
        self.image = self.original_image.copy()  # 描画用のSurfaceを作成(オリジナルのコピーを作成してimageにします)
        self.font = pygame.font.SysFont("Impact", 70)   #textフォントとサイズ
        self.update_text_surface

    def update(self):
        self.update_text_surface()

    def update_text_surface(self):
        self.text_surface = self.font.render(f"{self.life}",True,(255,255,255)) #表示させるtextと色
        text_surface_size = self.text_surface.get_size() #text_surfaceのサイズを取得、タプル型 (x,y)
        text_surface_center = (text_surface_size[0] // 2, text_surface_size[1] // 2)  #中心の特定
        image_center = (self.width // 2, self.height // 2) #imageの中心の特定
        self.blit_position = (image_center[0] - text_surface_center[0], image_center[1] - text_surface_center[1]) #中心座標へ
        self.image = self.original_image.copy()
        self.image.blit(self.text_surface,self.blit_position)


class mana(pygame.sprite.Sprite):
    def __init__(self,mana):
        pygame.sprite.Sprite.__init__(self)
        self.manaMax = mana    #引数で貰った初期mana
        self.manaCurrent = 1
        self.width = 180    #横幅
        self.height = 60   #縦幅
        self.x = 20
        self.y = 410
        self.fontSize = 40
        self.rect = Rect(self.x, self.y, self.width, self.height) #画像のx,y軸とサイズ
        self.original_image = pygame.image.load("img/mana_blue.png").convert_alpha()  # 画像を一度だけロード
        self.original_image = pygame.transform.scale(self.original_image, (self.width, self.height))  # 画像サイズをsurfaceのサイズに修正
        self.image = self.original_image.copy()  # 描画用のSurfaceを作成(オリジナルのコピーを作成してimageにします)
        self.font = pygame.font.SysFont("Impact", self.fontSize)   #textフォントとサイズ
        self.update_text_surface

    def update(self):
        self.update_text_surface()

    def update_text_surface(self):
        self.text_surface = self.font.render(f"{self.manaCurrent} / {self.manaMax}",True,(255,255,255)) #表示させるtextと色
        text_surface_size = self.text_surface.get_size() #text_surfaceのサイズを取得、タプル型 (x,y)
        text_surface_center = (text_surface_size[0] // 2, text_surface_size[1] // 2)  #中心の特定
        image_center = (self.width // 2, self.height // 2) #imageの中心の特定
        self.blit_position = (image_center[0] - text_surface_center[0], image_center[1] - text_surface_center[1]) #中心座標へ
        self.image = self.original_image.copy()
        self.image.blit(self.text_surface,self.blit_position)


        # self.liblaryCards = 20
        # self.graveyardCards = 0



# class GameInfo(pygame.sprite.Sprite):
#     def __init__(self, value, image_path, pos, size, font_size):
#         pygame.sprite.Sprite.__init__(self)
#         self.value = value
#         self.rect = pygame.Rect(*pos, *size)
#         self.original_image = pygame.image.load(image_path).convert_alpha()
#         self.original_image = pygame.transform.scale(self.original_image, size)
#         self.image = self.original_image.copy()
#         self.font = pygame.font.SysFont("Impact", font_size)
#         self.update_text_surface()

#     def update(self):
#         self.update_text_surface()

#     def update_text_surface(self):
#         self.text_surface = self.font.render(f"{self.value}", True, (255, 255, 255))
#         text_surface_size = self.text_surface.get_size()
#         text_surface_center = (text_surface_size[0] // 2, text_surface_size[1] // 2)
#         image_center = (self.rect.width // 2, self.rect.height // 2)
#         blit_position = (image_center[0] - text_surface_center[0], image_center[1] - text_surface_center[1])
#         self.image = self.original_image.copy()
#         self.image.blit(self.text_surface, blit_position)

# class Life(GameInfo):
#     def __init__(self, life):
#         super().__init__(life, "img/life.png", (300, 300), (200, 200), 70)

# class Mana(GameInfo):
#     def __init__(self, mana):
#         super().__init__(f"1 / {mana}", "img/mana_blue.png", (20, 410), (180, 60), 40)
