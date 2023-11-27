import pygame
from cardEffects import drawCard

class GM():
    def __init__(self):
        self.turn = True    #Trueで自分のターン
        self.battle = False #TrueでBattle描画開始
        self.preTurn = True
        self.win = False
        self.lose = False

    def judgeGame(self,pData,eData):
        if pData.life <= 0:
            self.islose()
        elif eData.life <= 0:
            self.iswin()

    def turnCheck(self):
        if self.turn != self.preTurn:
            self.preTurn = self.turn
            print("ターンが変わった")
            return True
        else:
            return False

    def turnEndProcess(self,pData,eData):
        if pData.mana > pData.manaMax:
            pData.mana = pData.manaMax
        if eData.mana > eData.manaMax:
            eData.mana = eData.manaMax
    
    def turnStartPlayer(self,pData,eData):
        pData.manaMax += 1
        pData.mana = pData.manaMax
        drawCard(pData,eData)
        drawCard(pData,eData)

    def turnStartEnemy(self,pData,eData):
        eData.manaMax += 1
        eData.mana = eData.manaMax


    def islose(self):
        print("時代の敗北者じゃけぇ")
        self.battle = False
        self.win = False
        self.lose = True
        # 次のマッチへのコード

    def iswin(self):
        print("大したやつだ…")
        self.battle = False
        self.win = True
        self.lose = False
        # なんかおまけのカードを貰って次のマッチへ行きたい。そうだろう

    def turnEnd(self):
        if self.turn == True:
            self.turn = False
            print("あなたのターンを終了しました")
        else:
            self.turn = True
            print("敵のターンを終了しました")