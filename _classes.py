import json


class Player:
    def __init__(self, hero: str):
        self.hero = hero
        self.inventory = set()

    def kill(self):
        pass
