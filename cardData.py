from card import Card
from cardEffects import *

# カードデータ集
cards = [
    {'id': 1, 'name': 'BlackLotus', 'cost': 100, 'text': '3マナ出るよ' ,'effect': BlackLotus, 'img':'img/BlackLotus.jpg'},
    {'id': 2, 'name': 'Brainstorm', 'cost': 100, 'text': 'カードいっぱい引きたい' ,'effect': Brainstorm, 'img':'img/Brainstorm.jpg'},
]


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
