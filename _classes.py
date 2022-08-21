from __future__ import annotations
from typing import List
from json import load, dump

team_lives: int = 4
night: bool = False


class Player:
    players: List[Player] = []

    def __init__(self, hero: str) -> None:
        self.hero = hero
        self.inventory: set = set()
        self.dead: bool = False
        with open('config.json', 'r') as file:
            config = load(file)['heroes'][hero]
        self.levels = config['level']


    def die(self) -> None:
        dead_players: List[Player] = []
        players = Player.players
        for player in players:
            if player.dead:
                dead_players.append(player)
        if len(dead_players) == len(players):
            for player in players:
                player.dead = False
            global team_lives
            team_lives -= 1
    
    def level_up(self) -> None:
        self.level += 1
        self.enchantment_points += 1

    @classmethod
    def create(cls, hero: str) -> Player:
        player = cls(hero)
        cls.players.append(player)
        return player
