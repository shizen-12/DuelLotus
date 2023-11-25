import pygame
import sys
from cardData import *
from card import Card
import os
from info import *
from deck import *

# Pygameの初期化
pygame.init()

SCREENRECT = pygame.Rect(0, 0, 1280, 720)
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

# 背景画像をロードしてスケーリング
background = pygame.image.load('img/bg.jfif')
background = pygame.transform.scale(background, (SCREENRECT.size))
screen.blit(background,(0,0))

# プレイヤーデータ画面表示用
manaValue = 1    #初期マナ
lifeValue = 20   #初期ライフ
libraryValue = 30   #初期ライブラリー
graveyardValue = 0  #初期墓地
manaInfo = Mana(manaValue)
lifeInfo = Life(lifeValue)
libraryInfo = Library(libraryValue)
graveyardInfo = Graveyard(graveyardValue)
player = Player()
playerInfo = pygame.sprite.Group()
playerInfo.add(manaInfo)
playerInfo.add(lifeInfo)
playerInfo.add(libraryInfo)
playerInfo.add(graveyardInfo)
playerInfo.add(player)

# エネミーデータ画面表示用
enemy1 = Enemy()
enemyLife = 20
eLifeInfo = EnemyLife(enemyLife)
enemyInfo = pygame.sprite.Group()
enemyInfo.add(enemy1)
enemyInfo.add(eLifeInfo)

# リストの作成
handAreaSize = 1080
handAreaStartX = 100
handGroup = pygame.sprite.Group()
graveyard = []
library = []
deck = [library, handGroup, graveyard]
decklist = loadDeck()
for n in decklist:
    library.append(createCard(n))

# handGroupの配置を変更する処理。
# for i文と同じ効果がある。nはインデックス cardは要素が入る。
def handSort():
    for n,card in enumerate(handGroup):
        card.rect.x = handAreaSize/(len(handGroup)+1)*(n+1)-card.width/2+handAreaStartX

def drawCard():
    if len(library) > 0:
        item = library.pop(0)
        handGroup.add(item)
        print("drawcardしたよ")


while True:
    display.blit(screen,(0,0))
    
    # イベント処理
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # キーイベント系処理
    if event.type == pygame.KEYDOWN:
        # print("キーが押された")
        if event.key == pygame.K_F1:
        # F1キーが押されたら全画面表示とウィンドウ表示を切り替え
            fullscreen = not fullscreen
            if fullscreen:
                display = pygame.display.set_mode(SCREENRECT.size,pygame.FULLSCREEN)
            else:
                display = pygame.display.set_mode(SCREENRECT.size)
            
        if event.key == pygame.K_ESCAPE:  # ESCキーが押されているかチェック
            break
        if event.key == pygame.K_LSHIFT:
            drawCard()


    # 背景描画
    screen.blit(background,(0,0))

    lifeInfo.life += 1
    manaInfo.manaCurrent += 1
    libraryInfo.library +=1
    graveyardInfo.graveyard +=1

    # スプライトの更新と描画
    handSort()
    handGroup.update()
    handGroup.draw(screen)
    playerInfo.update()
    playerInfo.draw(screen)
    enemyInfo.update()
    enemyInfo.draw(screen)

    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)


#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()