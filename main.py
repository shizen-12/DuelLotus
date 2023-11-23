import pygame
import sys
from cardData import *
from card import Card

# Pygameの初期化
pygame.init()

# 画面の初期化  pygame.RESIZABLEは窓のサイズ変更可能設定ちょっと怪しいので消すかも
screen = pygame.display.set_mode((1120, 630),pygame.RESIZABLE)

# タイトルの設定
pygame.display.set_caption("DuelLotus")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

# フルスクリーンフラグの初期化
fullscreen = False

#カードの作成
# c1 = card()
c1 = createCard(1)
c1.effect()



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
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((1120, 630))
        # ESCキーだったらゲーム終了
        if event.key == pygame.K_ESCAPE:
            break


    # 画面全体を塗りつぶす
    screen.fill((180,255,255))
    font1 = pygame.font.SysFont("Arial", 50)
    text1 = c1.name
    text_surface = font1.render(text1, True, (0,0,255))
    screen.blit(text_surface, (100,100))
    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)


#while文を抜けたらゲーム終了
pygame.quit()
sys.exit()