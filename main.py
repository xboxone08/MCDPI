import mcpi.minecraft as minecraft
from json import load, dump
from time import sleep

__all__ = tuple()

with open("config.json", 'r') as file:
    config = load(file)
heroes: dict = config["heroes"]
settings: dict = config["settings"]
hero: str = settings["default_hero"]
camera_angle: str = settings["camera_angle"]
fps: int = 1/settings["fps"]

if hero not in heroes:
    raise ValueError("Configured `hero` has not been defined in `heroes`.")
if camera_angle != "flat" and camera_angle != "angled":
    raise ValueError('`camera_angle` must be either "flat" or "angled".')

game = minecraft.Minecraft.create()

players = game.getPlayerEntityIds()

# Set up for Minecraft Dungeons
if camera_angle == "flat":
    game.camera.setFollow(players[0])

game.setting("world_immutable", True)

while True:
    if camera_angle == "angled":
        game.camera.setPos(game.player.getPos().x - 10,
                           game.player.getPos().y + 10,
                           game.player.getPos().z - 10)
    sleep(fps)
