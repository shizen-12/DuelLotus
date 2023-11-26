import pygame
from pygame.locals import *
from deck import *
from cardData import *
from card import *

# スプライトデータ郡、スプライトに文字列を配置するクラスの継承元
class GameInfo(pygame.sprite.Sprite):
    def __init__(self, image_path, pos, size, font_size, fontName,pdata):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(*pos, *size)
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, size)
        self.image = self.original_image.copy()
        self.font = pygame.font.SysFont(fontName, font_size)
        self.update(pdata)

    def update(self,charadata):   #ざっくりいうとそれぞれの中心をあわせて、イメージを貼り直してその上にテキストを更新して貼り直している
        self.text_surface = self.font.render(self.text(charadata), True, (255, 255, 255))
        text_surface_size = self.text_surface.get_size()
        text_surface_center = (text_surface_size[0] // 2, text_surface_size[1] // 2)
        image_center = (self.rect.width // 2, self.rect.height // 2)
        blit_position = (image_center[0] - text_surface_center[0], image_center[1] - text_surface_center[1])
        self.image = self.original_image.copy()
        self.image.blit(self.text_surface, blit_position)
    

class Life(GameInfo):
    def __init__(self,pdata):
        self.imgpath = "img/life.png"
        self.pos = (300,420)    #位置x,y
        self.size = (180,60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,pdata)
    def text(self,player):
        return f"{player.life}"

class Mana(GameInfo):
    def __init__(self,pdata):
        self.imgpath = "img/mana_blue.png"
        self.pos = (10, 420)    #位置x,y
        self.size = (180, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,pdata)
    def text(self,player):
        return f"{player.mana} / {player.manaMax}"

class Library(GameInfo):
    def __init__(self,pdata):
        self.imgpath = "img/library.png"
        self.pos = (10, 500)    #位置x,y
        self.size = (120, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,pdata)
    def text(self,player):
        return f"{len(player.library)}"
    
class Graveyard(GameInfo):
    def __init__(self,pdata):
        self.imgpath = "img/graveyard.png"
        self.pos = (10, 570)    #位置x,y
        self.size = (120, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,pdata)
    def text(self,player):
        return f"{len(player.graveyard)}"
    
# プレイヤーは文字データをスプライト上に表示しないのでGameInfoクラスを継承しない
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgpath = "img/player.jpg"
        self.pos = (250, 140)    #位置x,y
        self.size = (280, 280)   #サイズw,h
        self.rect = pygame.Rect(self.pos, self.size)
        self.image = pygame.image.load(self.imgpath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

# エネミーも同じく
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
    def __init__(self, edata):
        self.imgpath = "img/life.png"
        self.pos = (800,420)    #位置x,y
        self.size = (180,60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,edata)
    def text(self,edata):
        return f"{edata.life}"

class EnemyMana(GameInfo):
    def __init__(self, edata):
        self.imgpath = "img/mana_blue.png"
        self.pos = (1090, 50)    #位置x,y
        self.size = (180, 60)   #サイズw,h
        self.fontSize = 40
        self.fontName = "Impact"
        super().__init__(self.imgpath, self.pos, self.size, self.fontSize, self.fontName,edata)
    def text(self,edata):
        return f"{edata.mana} / {edata.manaMax}"
    

class PlayerData():
    def __init__(self):
        self.life = 20  
        self.mana = 1
        self.manaMax = 1
        self.graveyard = []
        self.library = []
        self.handGroup = pygame.sprite.LayeredUpdates()
        self.deck = [self.library, self.handGroup, self.graveyard]
        decklist = loadDeck()
        for n in decklist:
            self.library.append(createCard(n))
        self.playerInfo = pygame.sprite.Group()
    def createInfo(self):    
        self.playerInfo.add(Mana(self))
        self.playerInfo.add(Life(self))
        self.playerInfo.add(Library(self))
        self.playerInfo.add(Graveyard(self))
        self.playerInfo.add(Player())


class EnemyData():
    def __init__(self):
        self.life = 20
        self.mana = 1
        self.manaMax = 1
        self.enemyInfo = pygame.sprite.Group()

    def createInfo(self):    
        self.enemyInfo.add(EnemyMana(self))
        self.enemyInfo.add(EnemyLife(self))
        self.enemyInfo.add(Enemy())