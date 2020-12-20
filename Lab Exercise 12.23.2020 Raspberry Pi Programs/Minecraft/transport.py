import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
block = 38
while True:
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        mc.setBlock(x, y, z, block)
        time.sleep(0.2)

