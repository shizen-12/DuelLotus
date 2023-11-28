# カード効果集
# 関数名はカード名と同名にすること
# deck = [library, handGroup, graveyard]
# カードエフェクトの引数はすべてpData,eData
# 汎用ワードエフェクトは引数は任意
from pygame.locals import *
import pygame
# 音声ファイルのロード
pygame.mixer.init()
soundDmg = pygame.mixer.Sound("se/damaged4.mp3")
soundDraw = pygame.mixer.Sound("se/draw.mp3")
soundDraw.set_volume(0.2)
soundGainLife = pygame.mixer.Sound("se/gainlife.mp3")
soundGainLife.set_volume(0.5)
soundLotus = pygame.mixer.Sound("se/lotus.mp3")

class effectSprite(pygame.sprite.Sprite):
    def __init__(self,imgpath,xvalue,yvalue,mount,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(imgpath)
        # スプライトシートから個々のフレームを取得
        self.frames = []
        spriteXvalue = xvalue
        spriteYvalue = yvalue
        spriteMount = mount
        self.frame_width = self.image.get_width() / spriteXvalue
        self.frame_height = self.image.get_height() / spriteYvalue
        for j in range(spriteYvalue):
            for i in range(spriteXvalue):
                if j * spriteXvalue + i >= spriteMount:
                    break
                frame = self.image.subsurface((i * self.frame_width, j * self.frame_height, self.frame_width, self.frame_height))
                self.frames.append(frame)
        # アニメーションフレームのインデックス
        self.frame_index = 0
        # self.image = self.frames[self.frame_index]
        self.image = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA) #最初は透明にする
        self.effectPlaying = False
        self.rect = Rect(self.x, self.y, self.frame_width, self.frame_height)   #spriteの表示位置
    
    def update(self):
        if self.effectPlaying:
            if self.frame_index < len(self.frames):
                self.image = self.frames[self.frame_index]
                self.frame_index += 1
            else:
                self.effectPlaying = False
                self.frame_index = 0  # アニメーションをリセット
                # アニメーションが終了したら透明な画像に戻す
                self.image = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)


enemyX = 800
enemyY = 160
playerX = 300
playerY = 160
libraryX = -20
libraryY = 390
effectSpriteGroup = pygame.sprite.Group()
effectFire = effectSprite("img/fireballsheet.png",5,3,14,enemyX,enemyY)
effectCure = effectSprite("img/cure.png",5,2,10,playerX,playerY)
effectDraw = effectSprite("img/recovery_A.png",5,3,13,libraryX,libraryY)
effectMana = effectSprite("img/attackBurst.png",5,3,15,playerX,playerY)
effectEFire = effectSprite("img/fireballsheet.png",5,3,14,playerX,playerY)

effectSpriteGroup.add(effectFire)
effectSpriteGroup.add(effectCure)
effectSpriteGroup.add(effectDraw)
effectSpriteGroup.add(effectMana)
effectSpriteGroup.add(effectEFire)



def effectUpdate(self):
    if self.frame_index != 0:
        self.image = self.frames[self.frame_index]
        self.frame_index = (self.frame_index + 1) % len(self.frames)

def drawCard(pData,eData):
    if len(pData.deck[0]) > 0:
        item = pData.deck[0].pop(0)
        pData.deck[1].add(item)

def toGraveyard(pData,eData):
    pData.deck[1].pop()

def damagePtE(eData,dmg):
    eData.life -= dmg
    soundDmg.play()

def damageEtP(pData,dmg):
    pData.life -= dmg
    soundDmg.play()

def manaUp(data,mana):
    data.mana += mana
    
MirageLotus_text = "3マナ加える"
def MirageLotus(pData,eData):
    manaUp(pData,3)
    soundLotus.play()
    effectMana.effectPlaying = True


Brainstorm_text = "カードを3枚引く"
def Brainstorm(pData,eData):
    drawCard(pData,eData)
    drawCard(pData,eData)
    drawCard(pData,eData)
    soundDraw.play()
    effectDraw.effectPlaying = True

FireBall_text = "3点ダメージ"
def FireBall(pData,eData):
    damagePtE(eData,3)
    effectFire.effectPlaying = True
def eFireBall(pData,eData):
    damageEtP(pData,3)
    effectEFire.effectPlaying = True
def eFireBallTriple(pData,eData):
    damageEtP(pData,3)
    effectEFire.effectPlaying = True
    damageEtP(pData,3)
    effectEFire.effectPlaying = True
    damageEtP(pData,3)
    effectEFire.effectPlaying = True
    soundDmg.play()

LifeRoad_text = "5点回復"
def LifeRoad(pData,eData):
    pData.life += 5
    soundGainLife.play()
    effectCure.effectPlaying = True

Lightning_text = "5点ダメージ"
def Lightning(pData,eData):
    damagePtE(pData,5)
    effectFire.effectPlaying = True