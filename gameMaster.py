import pygame
from cardEffects import drawCard

class GM():
    def __init__(self):
        self.turn = True    #Trueで自分のターン
        self.battle = False #TrueでBattle描画開始


    def judgeGame(self,pData,eData):
        if pData.life <= 0:
            self.lose()
        elif eData.life <= 0:
            self.win()

    def turnEnd(self,pData,eData):
        if pData.mana > pData.manaMax:
            pData.mana = pData.manaMax
        if eData.mana > eData.manaMax:
            eData.mana = eData.manaMax
    
    def turnStartPlayer(self,pData,eData):
        pData.manaMax += 1
        pData.mana = pData.manaMax
        drawCard(pData,eData)
        drawCard(pData,eData)

    def turnStartEnemy(self):
        print("敵のターンスタートだけど特にやることない、多分エフェクトとか入れるのでここに書く")

    def lose(self):
        print("時代の敗北者じゃけぇ")
        # 次のマッチへのコード

    def win(self):
        print("大したやつだ…")
        # なんかおまけのカードを貰って次のマッチへ行きたい。そうだろう