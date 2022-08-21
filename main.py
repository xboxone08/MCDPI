import mcpi.minecraft as minecraft
from json import load, dump
from time import sleep

with open("config.json", 'r') as conf_file:
    config = load(conf_file)
heroes: dict = config["heroes"]
settings: dict = config["settings"]
hero: str = settings["default_hero"]
camera_angle: str = settings["camera_angle"]
fps: int = 1/settings["fps"]

assert(hero in heroes)
assert(camera_angle == "flat" or camera_angle == "angled")

game = minecraft.Minecraft.create()

player_id = game.getPlayerEntityIds()[0]

# Set up for Minecraft Dungeons
if camera_angle == "flat":
    game.camera.setFollow(player_id)

game.setting("world_immutable", True)

while True:
    if camera_angle == "angled":
        game.camera.setPos(game.player.getPos().x - 10,
                           game.player.getPos().y + 10,
                           game.player.getPos().z - 10)
    sleep(fps)
