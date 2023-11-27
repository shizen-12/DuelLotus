# カード効果集
# 関数名はカード名と同名にすること
# deck = [library, handGroup, graveyard]
# カードエフェクトの引数はすべてpData,eData
# 汎用ワードエフェクトは引数は任意

def drawCard(pData,eData):
    if len(pData.deck[0]) > 0:
        item = pData.deck[0].pop(0)
        pData.deck[1].add(item)

def toGraveyard(pData,eData):
    pData.deck[1].pop()

def damagePtE(eData,dmg):
    eData.life -= dmg

def damageEtP(pData,dmg):
    pData.life -= dmg

def manaUp(data,mana):
    data.mana += mana
    
MirageLotus_text = "3マナ加える"
def MirageLotus(pData,eData):
    manaUp(pData,3)

Brainstorm_text = "カードを3枚引く"
def Brainstorm(pData,eData):
    drawCard(pData,eData)
    drawCard(pData,eData)
    drawCard(pData,eData)

FireBall_text = "2点ダメージ"
def FireBall(pData,eData):
    damagePtE(eData,10)

LifeRoad_text = "5点回復"
def LifeRoad(pData,eData):
    pData.life += 5