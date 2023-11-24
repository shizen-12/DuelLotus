import pygame
from pygame.locals import *

class Card(pygame.sprite.Sprite):
    width = 189
    height = 267
    x = 300
    y = 300
    def __init__(self, id, name, cost, text, effect, imgpath):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.name = name
        self.cost = cost
        self.text = text
        self.effect = effect
        self.imgpath = imgpath
        self.image = pygame.image.load(self.imgpath).convert()
        resizedImage = pygame.transform.scale(self.image,(self.width,self.height))
        self.rect = Rect(self.x, self.y, self.width, self.height)   #spriteの表示位置
        self.vx = 0     #x軸の移動速度
        self.vy = 0     #y軸の移動速度

    def effect(self):
        # effect関数の実装
        pass

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # if self.rect.left < 0 or self.rect.right > SURFACE.width:
        #     self.vx = -self.vx
        # if self.rect.top < 0 or self.rect.bottom > SURFACE.height:
        #     self.vy = -self.vy
        # self.rect = self.rect.clamp(SURFACE)

    def draw(self, surface):
        surface.blit(self.image, self.rect)