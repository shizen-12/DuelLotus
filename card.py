import pygame
from pygame.locals import *

class Card(pygame.sprite.Sprite):
    highlight = False
    select = False
    
    x = 100
    y = 480
    def __init__(self, id, name, cost, text, effect, imgpath):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.name = name
        self.cost = cost
        self.text = text
        self.effect = effect
        self.imgpath = imgpath
        self.width = 170
        self.height = 237
        self.prev_select = self.select
        self.prev_highlight = self.highlight
        self.original_image = pygame.image.load(self.imgpath).convert()
        # self.original_image = pygame.transform.scale(self.original_image,(self.width,self.height))    スケール調整はpygameは汚いのであまり使わない
        self.selected_image = pygame.image.load("img/select.png").convert_alpha()
        # self.selected_image = pygame.transform.scale(self.selected_image,(40,40))
        self.image = self.original_image.copy()
        self.rect = Rect(self.x, self.y, self.width, self.height)   #spriteの表示位置
        self.vx = 0     #x軸の移動速度
        self.vy = 0     #y軸の移動速度
        self.update()
        
    def effect(self):
        # effect関数の実装
        pass

    def highlighted(self):
        if self.highlight == True:
            ratio = 1.1 #拡大倍率
            self.image = pygame.transform.scale(self.image,(self.width*ratio,self.height*ratio))
            if self.rect.y > self.y - self.height * (ratio-1):
                self.rect.y -= self.height * (ratio-1)
        else:
            self.rect.y = self.y
    
    def selected(self):
        if self.select == True:
            self.image.blit(self.selected_image,(0,self.image.get_height()-40))


    def update(self):
        if self.select != self.prev_select or self.highlight != self.prev_highlight:
            self.image = self.original_image.copy()
            self.highlighted()
            self.selected()
        self.prev_select = self.select
        self.prev_highlight = self.height
        
        font = pygame.font.SysFont("yumincho", 18, bold=True)
        self.text_surface = font.render(self.text, True, (0, 0, 0))
        text_surface_size = self.text_surface.get_size()
        text_surface_center = (text_surface_size[0] // 2 ,text_surface_size[1] //2)
        blit_position = (self.image.get_width()//2 - text_surface_center[0],self.image.get_height()*0.75-text_surface_center[1])
        self.image.blit(self.text_surface, blit_position)
    
        font = pygame.font.SysFont("Arial", 32, bold=True)
        self.text_surface = font.render(f"{self.cost}", True, (0, 0, 0))
        blit_position = (13,2)
        self.image.blit(self.text_surface, blit_position)

        font = pygame.font.SysFont("Arial", 20, bold=True)
        self.text_surface = font.render(self.name, True, (0, 0, 0))
        text_surface_size = self.text_surface.get_size()
        text_surface_center = (text_surface_size[0] // 2 ,text_surface_size[1] //2)
        blit_position = (self.image.get_width()*0.55 - text_surface_center[0],self.image.get_height()*0.07-text_surface_center[1])
        self.image.blit(self.text_surface, blit_position)
        

    def draw(self, surface):
        surface.blit(self.image, self.rect)