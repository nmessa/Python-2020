import  mcpi.minecraft as minecraft
import  mcpi.block as block

mc = minecraft.Minecraft.create()
SIZE = 20
air = block.AIR.id
window = block.GLASS.id
roof = block.WOOD.id
floor = block.GOLD_ORE.id

def  buildGreenHouse():
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, window) 
    mc.setBlocks(x+1, y+1, z+1, x+SIZE-2, y+SIZE-2, z+SIZE-2, air)
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, roof)
    mc.setBlocks(x+1, y+1, z+1, x+SIZE-1, y+1, z+SIZE-1, floor) 

pos = mc.player.getTilePos()
x = pos.x + 2
y = pos.y
z = pos.z
buildGreenHouse()

