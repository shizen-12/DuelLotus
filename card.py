import pygame
from pygame.locals import *

class Card(pygame.sprite.Sprite):

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
        self.height = 240       
        self.original_image = pygame.image.load(self.imgpath).convert()
        self.original_image = pygame.transform.scale(self.original_image,(self.width,self.height))
        self.image = self.original_image.copy()
        self.rect = Rect(self.x, self.y, self.width, self.height)   #spriteの表示位置

        self.vx = 0     #x軸の移動速度
        self.vy = 0     #y軸の移動速度

    def effect(self):
        # effect関数の実装
        pass

    def selected(self):
        ratio = 1.1 #拡大倍率
        self.image = pygame.transform.scale(self.image,(self.width*ratio,self.height*ratio))
        if self.rect.y > self.y - self.height * (ratio-1):
            self.rect.y -= self.height * (ratio-1)
    
    def notSelected(self):
        self.image = self.original_image.copy()
        self.rect.y = self.y

    def update(self, mousePos):
        # if self.x < mousePos(0) < self.x + self.width and self.y < mousePos(1) < self.y + self.height :
        # 上をスマートにしたやつが下
        if self.rect.collidepoint(mousePos):
            self.selected()
        else :
            self.notSelected()


    def draw(self, surface):
        surface.blit(self.image, self.rect)