import pygame
import sys
from cardData import *
from card import Card
import os

# Pygameの初期化
pygame.init()

SCREENRECT = pygame.Rect(0, 0, 1120, 630)
# 画面の初期化  pygame.RESIZABLEは窓のサイズ変更可能設定ちょっと怪しいので消すかも
screen1 = pygame.display.set_mode(SCREENRECT.size, pygame.RESIZABLE)
screen = pygame.Surface(SCREENRECT.size)
# タイトルの設定
pygame.display.set_caption("DuelLotus")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

# フルスクリーンフラグの初期化
fullscreen = False
thisDisplay = pygame.display.Info()
displayWidth = thisDisplay.current_w
displayHeight = thisDisplay.current_h


#カードの作成
c1 = createCard(1)
c2 = createCard(2)

# リストの作成
hand = []
graveyard = []
library = []
deck = [library, hand, graveyard]

# カードをリストに入れてみる
hand.append(c1)
hand.append(c2)

# カードsurfaceの作成
cardsurface = pygame.Surface((189,267))
image = pygame.image.load("img/BlackLotus.jpg")
resizedImage = pygame.transform.scale(image,(189,267))
cardsurface.blit(resizedImage,(0,0))


while True:

    # イベント処理
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # キーイベント系処理
    if event.type == pygame.KEYDOWN:
        # F1キーが押されたら全画面表示とウィンドウ表示を切り替え
        if event.key == pygame.K_F1:
            fullscreen = not fullscreen
            if fullscreen:
                # screen_backup = screen.copy()
                
                screen1 = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                pygame.transform.scale(screen, (pygame.display.get_surface().get_size()),pygame.display.get_surface())
                # screen.blit(screen_backup, (0, 0))
            else:
                screen1 = pygame.display.set_mode(SCREENRECT.size)
                screen1.blit(screen,(0,0))
        # ESCキーだったらゲーム終了
        if event.key == pygame.K_ESCAPE:
            break


    # 画面全体を塗りつぶす
    screen.fill((180,255,255))
    font1 = pygame.font.SysFont("Arial", 50)
    text1 = c1.name
    text_surface = font1.render(text1, True, (0,0,255))
    screen.blit(text_surface, (100,100))
    screen.blit(cardsurface,(300,300))

    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)


#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()