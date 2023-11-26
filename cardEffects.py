# カード効果集
# 関数名はカード名と同名にすること
# deck = [library, handGroup, graveyard]

def drawCard(deck):
    if len(deck[0]) > 0:
        item = deck[0].pop(0)
        deck[1].add(item)

def damaged(character,dmg):
    character.life -= dmg

def BlackLotus():
    print("ブラックロータスだよ")

def Brainstorm():
    print("brainstormだよ")