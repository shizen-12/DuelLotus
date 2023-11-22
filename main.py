import pygame
import sys
# 色の定義
BLACK = (0, 0, 0)

# Pygameの初期化
pygame.init()

# 画面の初期化
screen = pygame.display.set_mode((1120, 630))

# タイトルの設定
pygame.display.set_caption("画面の色")

# 時間管理用のオブジェクトの作成
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # ウィンドウの閉じるボタンがクリックされたら終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 画面全体を黒で塗りつぶす
    screen.fill(BLACK)

    # 画面を更新
    pygame.display.update()

    # フレームレートを設定（1秒間に30回処理）
    clock.tick(30)

