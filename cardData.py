from card import Card
from cardEffects import *

# カードデータ集
cards = [
    {'id': 1, 'name': 'MirageLotus', 'cost': 0, 'text': MirageLotus_text ,'effect': MirageLotus, 'img':'img/miragelotus.png'},
    {'id': 2, 'name': 'Brainstorm', 'cost': 1, 'text': Brainstorm_text ,'effect': Brainstorm, 'img':'img/magicitem.png'},
    {'id': 3, 'name': 'FireBall', 'cost': 2, 'text': FireBall_text ,'effect': FireBall, 'img':'img/fireball.png'},
    {'id': 4, 'name': 'LifeRoad', 'cost': 3, 'text': LifeRoad_text ,'effect': LifeRoad, 'img':'img/liferoad.png'},
    {'id': 5, 'name': 'eFireBall', 'cost': 2, 'text': FireBall_text ,'effect': eFireBall, 'img':'img/fireball.png'},
    {'id': 6, 'name': 'eFireBallTriple', 'cost': 4, 'text': FireBall_text ,'effect': eFireBallTriple, 'img':'img/fireball.png'},
    {'id': 7, 'name': 'Lightning', 'cost': 3, 'text': Lightning_text ,'effect': Lightning, 'img':'img/lightning.png'},

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
