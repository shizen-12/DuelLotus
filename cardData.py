from card import Card
from cardEffects import *

# カードデータ集
cards = [
    {'id': 1, 'name': 'BlackLotus', 'cost': 100, 'text': '3マナ出るよ' ,'effect': BlackLotus, 'img':'imgpath'},
    {'id': 2, 'name': 'BrainStorm', 'cost': 100, 'text': 'text' ,'effect': BlackLotus, 'img':'imgpath'},
]


# # 関数を呼び出す
# cards[0]["effect"]()
# print(cards[0]["effect"])
# print("testttt")

# cardを探し出す関数
def get_card(id):
    for card in cards:
        if card['id'] == id:
            return card
    return None

# インスタンスの作成
def createCard(id):
    cardData = get_card(id)
    card = Card(cardData["id"],cardData["name"],cardData["cost"],cardData["text"], cardData["effect"], cardData["img"])
    return card