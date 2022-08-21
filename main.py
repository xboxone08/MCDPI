import mcpi.minecraft as minecraft
from json import load, dump
from time import sleep

__all__ = tuple()

with open("config.json", 'r') as file:
    config = load(file)
heroes: dict = config["heroes"]
settings: dict = config["settings"]
hero: str = settings["default_hero"]
fps: int = 1/settings["fps"]

if hero not in heroes:
    raise ValueError("Configured `hero` has not been defined in `heroes`.")

game = minecraft.Minecraft.create()

players = game.getPlayerEntityIds()

# Set up for Minecraft Dungeons
game.camera.setFollow(players[0])

game.setting("world_immutable", True)

while True:
    sleep(fps)
