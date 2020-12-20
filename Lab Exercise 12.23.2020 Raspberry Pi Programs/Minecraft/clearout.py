import  mcpi.minecraft as minecraft
import  mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

x = pos.x
y = pos.y
z = pos.z
air = block.AIR.id

mc.setBlocks(x-50, y, z-50, x+150, y+150, z+150, air)
