import pygame
import sys
from cardData import *
from info import *
from deck import *
from gameMaster import *

# Pygameの初期化
pygame.init()

# 画面の初期化
SCREENRECT = pygame.Rect(0, 0, 1280, 720)
screen = pygame.display.set_mode(SCREENRECT.size)  #最終表示用のsurface
screen = pygame.Surface(SCREENRECT.size)           #拡大縮小対応用の描画領域、ここに描画する

# タイトルの設定
pygame.display.set_caption("DuelLotus")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

# フルスクリーンフラグの初期化
fullscreen = False

# 背景画像をロードしてスケーリング
background = pygame.image.load('img/bg1.jpg')
background = pygame.transform.scale(background, (SCREENRECT.size))
screen.blit(background,(0,0))

#ゲームマスターの作成
gm = GM()
gm.battle = True
# print(pygame.font.get_fonts())

#プレイヤーとエネミーの作成
pData = PlayerData()
pData.createInfo()
eData = EnemyData()
eData.createInfo()

#マウス座標
mousePos = (0,0)
mouse_down = False
mouse_clicked = False

# handGroupの配置を変更する処理。
# for i文と同じ効果がある。nはインデックス cardは要素が入る。
handAreaSize = 1080
handAreaStartX = 100
def handSort():
    for n,card in enumerate(pData.handGroup):
        card.rect.x = handAreaSize/(len(pData.handGroup)+1)*(n+1)-card.width/2+handAreaStartX
        if card.rect.collidepoint(mousePos) and mousePos[0] < handAreaSize/(len(pData.handGroup)+1)*(n+2)-card.width/2+handAreaStartX:
            card.highlight = True
        elif card.rect.collidepoint(mousePos) and n == len(pData.handGroup) -1:
            card.highlight = True
        else:
            card.highlight = False
def handHighlightedDraw():
    for card in pData.handGroup:
        if card.highlight == True:
            screen.blit(card.image, card.rect)

def handOnClick():
    # 一度選択を全解除
    for card in pData.handGroup:
        card.select = False
    # その後ハイライトされていたら選択状態に変更
    for card in pData.handGroup:
        if card.highlight == True:
            card.select = True

def doubleClickCheck():
    for card in list(pData.handGroup):  #list(pData.handGroup)で一時的なコピー作成
        if card.rect.collidepoint(mousePos) and card.select == True:
            if pData.mana >= card.cost:
                card.effect(pData,eData)
                pData.mana -= card.cost
                pData.handGroup.remove(card)  # 元のリストからカードを削除
                pData.graveyard.append(card)  # graveyardリストにカードを追加

timer = 0
dt = 0



while gm.battle == True:
    # 背景描画
    screen.blit(background,(0,0))

    # スプライトの更新と描画
    handSort()
    pData.handGroup.update()
    # changeLayer()
    pData.handGroup.draw(screen)
    handHighlightedDraw()
    pData.playerInfo.update(pData)
    pData.playerInfo.draw(screen)
    eData.enemyInfo.update(eData)
    eData.enemyInfo.draw(screen)

    # Surfaceの内容をディスプレイに反映
    pygame.display.get_surface().blit(screen, (0, 0))
    pygame.display.flip()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)

    # イベント処理
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # キーイベント系処理
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
        # F1キーが押されたら全画面表示とウィンドウ表示を切り替え
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode(SCREENRECT.size,pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode(SCREENRECT.size)
            
        if event.key == pygame.K_ESCAPE:  # ESCキーが押されているかチェック
            break
        if event.key == pygame.K_LSHIFT:
            drawCard(pData,eData)
        if event.key == pygame.K_LEFT:
            print(event.key)
        if event.key == pygame.K_RIGHT:
            print(event.key)

    # ここからマウス系処理
    if event.type == MOUSEMOTION:
        mousePos = pygame.mouse.get_pos()
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:   #左クリック
            if not mouse_down:
                mouse_down = True
                mouse_clicked = True
                if timer == 0:  # 最初のクリック
                    timer = 0.001  # タイマーを開始
                elif timer < 0.25:  #ダブルクリックの感覚
                    doubleClickCheck()
                    timer = 0
    if event.type == MOUSEBUTTONUP:
        if event.button == 1:
            mouse_down = False

    # 最初のクリック後にタイマーを増加
    if timer != 0:
        timer += dt
    if timer >= 0.25:
        timer = 0

    dt = clock.tick(60) / 1000  #1Fごとに16msくらい0.016くらい加算されるよ

    if mouse_clicked:
        handOnClick()
        mouse_clicked = False

#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()