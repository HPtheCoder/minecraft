from mcpi.minecraft import Minecraft

import time

mc = Minecraft.create() 



#portal 1

x1, y1, z1 = mc.player.getTilePos()



#skapa portal 1

mc.setBlocks(x1, y1, z1-1, x1, y1+2,  z1+1, 246)

#INGÅNG
mc.setBlocks(x1, y1, z1, x1, y1+1, z1, 0)







# portal 2
x2 = 474
y2 = 123
z2 = 145




#skapa portal 2
mc.setBlocks(x2-1, y2, z2, x2+1, y2+2, z2, 246)

# ingång 2
mc.setBlocks(x2, y2, z2, x2, y2+1, z2, 0)



block_synlig = True


while True:

    time.sleep(0.5)

    x, y, z = mc.player.getTilePos()

    if x == x1 and y == y1 and z ==z1:
        mc.player.setTilePos(x2, y2, z2+2)
    elif x == x2 and y == y2 and z == z2:
        mc.player.setTilePos(x1+2, y1, z1)

    # blinkande block
    if block_synlig:
        mc.setBlock(x1, y1+3, z1, 0)
        mc.setBlock(x2, y2+3, z2, 0)
        block_synlig = False
    else:
        mc.setBlock(x1, y1+3, z1, 89)
        mc.setBlock(x2, y2+3, z2, 89)
        block_synlig = True

