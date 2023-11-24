import pygame
import sys
from cardData import *
from card import Card
import os

# Pygameの初期化
pygame.init()

SCREENRECT = pygame.Rect(0, 0, 1120, 630)
# 画面の初期化
display = pygame.display.set_mode(SCREENRECT.size)  #最終表示用のsurface
screen = pygame.Surface(SCREENRECT.size)            #拡大縮小対応用の描画領域、ここに描画する
display.blit(screen,(0,0))

# タイトルの設定
pygame.display.set_caption("DuelLotus")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

# フルスクリーンフラグの初期化
fullscreen = False
thisDisplay = pygame.display.Info() #ユーザーのディスプレイサイズの取得
displayWidth = thisDisplay.current_w
displayHeight = thisDisplay.current_h

# 背景画像をロードしてスケーリング
background = pygame.image.load('img/bg.jfif')
background = pygame.transform.scale(background, (SCREENRECT.size))
screen.blit(background,(0,0))

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
image = pygame.image.load("img/BlackLotus.jpg").convert()
resizedImage = pygame.transform.scale(image,(189,267))
cardsurface.blit(resizedImage,(0,0))
# hand[0].createSurface()

handGroup = pygame.sprite.Group()
handGroup.add(c1)
while True:
    if not fullscreen:
        display.blit(screen,(0,0))
    # イベント処理
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # キーイベント系処理
    if event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()  # キーの状態を取得
        # F1キーが押されたら全画面表示とウィンドウ表示を切り替え
        if keys[pygame.K_F1]:  # F1キーが押されているかチェック
            fullscreen = not fullscreen
            if fullscreen:
                display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
                pygame.transform.scale(screen, (pygame.display.get_surface().get_size()),pygame.display.get_surface())
            else:
                display = pygame.display.set_mode(SCREENRECT.size)
                display.blit(screen,(0,0))
        if keys[pygame.K_ESCAPE]:  # ESCキーが押されているかチェック
            break

    # 背景描画
    screen.blit(background,(0,0))
    screen.blit(cardsurface,(300,300))
    # スプライトの更新と描画
    handGroup.update()
    handGroup.draw(screen)

    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)


#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()