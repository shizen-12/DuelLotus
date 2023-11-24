import pygame
from pygame.locals import *

class life(pygame.sprite.Sprite):
    def __init__(self,life):
        pygame.sprite.Sprite.__init__(self)
        self.life = life
        self.width = 200
        self.height = 200
        self.rect = Rect(300, 300, self.width, self.height) 
        self.image = pygame.image.load("img/life.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.font = pygame.font.SysFont("Arial", 50)
        self.text_surface = self.font.render(f"{self.life}",True,(255,255,255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        # self.text_rect = Rect(300, 300, self.width, self.height)
        self.image.blit(self.text_surface,self.text_rect)
        print(self.text_rect)
        print(f"{self.life}")

    def draw(self, surface):
        self.image.blit(self.text_surface,self.text_rect)
        surface.blit(self.image, self.rect)
        # surface.blit(self.text_surface,self.text_rect)


class mana(pygame.sprite.Sprite):
    def __init__(self,mana):
        pygame.sprite.Sprite.__init__(self)
        self.maxMana = mana
        self.currentMana = 1
        self.width = 300
        self.height = 80
        self.rect = Rect(30, 400, self.width, self.height) 
        self.image = pygame.image.load("img/mana.jpg").convert()
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.font = pygame.font.SysFont("Arial", 25)
        self.text_surface = self.font.render(f"{self.currentMana}/{self.maxMana}",True,(255,255,255))
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.image.blit(self.text_surface,text_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



        # self.liblaryCards = 20
        # self.graveyardCards = 0