from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

höjd = 5
bredd = 10
längd = 10

# skapa hus av trä
plankor_block = 5
mc.setBlocks(x, y, z, x+längd, y+höjd, z+bredd, plankor_block)

# tomt inuti
mc.setBlocks(x+1, y, z+1, x+längd-1, y+höjd-1,  z+bredd-1, 0)
 # gör håll
mc.setBlocks(x, y, z+3, x, y+1, z+3, 0)

# skapa dörr
dörr_block = 64
mc.setBlock(x, y, z+3 ,dörr_block, 4)
mc.setBlock(x, y+1, z+3 ,dörr_block, 8)

# skapar fönster
glas = 20
mc.setBlocks(x+1, y+1, z, x+längd-1, y+3, z, glas)

# skapa tak
tak_block = 209
mc.setBlocks(x-1, y+4, z-1, x+längd+1, y+4, z+bredd+1, tak_block)

# skapa fackla
fackla_block = 50
mc.setBlock(x-1, y+1, z+2, fackla_block, 2)

mc.setBlock(x-1, y+1, z+4, fackla_block, 2)

#sova
sova_Block = 26
mc.setBlock(x+6, y, z+8, sova_Block, 0)
mc.setBlock(x+6, y, z+9, sova_Block, 8)
45

# ljus
mc.setBlock(x+2, z+5, y+1, fackla_block, 4)
