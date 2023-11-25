import json

def saveDeck(deckList):
    with open("save.json", "w") as f:
        json.dump(deckList,f)

def loadDeck():
    with open("save.json", "r") as f:
        deckList = json.load(f)
    return deckList

