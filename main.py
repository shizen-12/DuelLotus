import pygame
import sys
from cardData import *
from info import *
from deck import *

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
background = pygame.image.load('img/bg.jfif')
background = pygame.transform.scale(background, (SCREENRECT.size))
screen.blit(background,(0,0))

#プレイヤーとエネミーの作成
pData = PlayerData()
pData.createInfo()
eData = EnemyData()
eData.createInfo()

#マウス座標
mousePos = (0,0)

# handGroupの配置を変更する処理。
# for i文と同じ効果がある。nはインデックス cardは要素が入る。
handAreaSize = 1080
handAreaStartX = 100
def handSort():
    for n,card in enumerate(pData.handGroup):
        card.rect.x = handAreaSize/(len(pData.handGroup)+1)*(n+1)-card.width/2+handAreaStartX



while True:
    # 背景描画
    screen.blit(background,(0,0))
    pData.life += 1

    # スプライトの更新と描画
    handSort()
    pData.handGroup.update(mousePos)
    pData.handGroup.draw(screen)
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
            drawCard(pData.deck)
        if event.key == pygame.K_LEFT:
            print(event.key)
        if event.key == pygame.K_RIGHT:
            print(event.key)

    # ここからマウス系処理
    if event.type == MOUSEMOTION:
        mousePos = pygame.mouse.get_pos()


#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()