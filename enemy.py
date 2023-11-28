import deck
from cardData import *
class EnemyBehavior():
    aciton1 = 0
    action2 = 0
    action3 = 0
    action4 = 0
    action5 = 0
    library = []
    def __init__(self):
        decklist = deck.loadDeck("saveEnemy1.json")
        for n in decklist:
            self.library.append(createCard(n))
    def thinking(self,pData,eData,gm):
        # 行動パターンをいくつかの要素に分けて判断
        enemyPlayable = True
        while enemyPlayable:
            # self.action(pData,eData,1)
            print("ループに入った")
            for card in self.library:
                print("for文に入った")
                if eData.mana >= card.cost:
                    print("if文に入った")
                    card.effect(pData,eData)
                    eData.mana -= card.cost
                else:
                    enemyPlayable = False
                    print("enemyPlayableがFalseになった")
        # if eData.mana <= 0:
        #     print("gm.turnEnd()を呼び出します")
        gm.turnEnd()


    def action(self,pData,eData,num):
        if num == 1:
            print("action1を使用した")
            pData.life -= 2
            eData.mana -= 1
