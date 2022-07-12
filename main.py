import mcpi.minecraft as minecraft

game = minecraft.Minecraft.create()

player = game.getPlayerEntityIds()[0]

# Set up for Minecraft Dungeons
game.camera.setFollow(player)
game.setting("world_immutable", True)

while True:
    
