import pygame
import sys
import card
# 色の定義
BLACK = (0, 0, 0)

# Pygameの初期化
pygame.init()

# 画面の初期化
screen = pygame.display.set_mode((1120, 630))

# タイトルの設定
pygame.display.set_caption("DuelLotus")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

# フルスクリーンフラグの初期化
fullscreen = False

#カードの作成
c1 = card

while True:
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # F1キーが押されたら全画面表示とウィンドウ表示を切り替え
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((1120, 630))

    # 画面全体を黒で塗りつぶす
    screen.fill(BLACK)
    font1 = pygame.font.SysFont("Arial", 50)
    text1 = "c1.name"
    screen.blit(text1,(40,30))
    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(60)

