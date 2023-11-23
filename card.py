class Card:
    def __init__(self, id, name, cost, text, effect, imgpath):
        self.id = id
        self.name = name
        self.cost = cost
        self.text = text
        self.effect = effect
        self.imgpath = imgpath

    def effect(self):
        # effect関数の実装
        pass