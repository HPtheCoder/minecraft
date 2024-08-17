import mcpi.minecraft as minecraft
import random
import time

#beräkna avstånd från spelare till ett block
def block_avstånd(block_x, block_y, block_z, pos):
    avstånd_x = pos.x - block_x
    avstånd_y = pos.y - block_y
    avstånd_z = pos.z - block_z

    # pythagoras sats för att beräkna avstånd
    avstånd = (avstånd_x** 2 +avstånd_y ** 2 + avstånd_z ** 2) ** 0.5

    return avstånd


# skapa slumpmässig block på slumpmässig position och returner positon
def skapa_block(pos, avstånd):
    x = random.randint(int(pos.x - avstånd), int(pos.x + avstånd))
    z = random.randint(int(pos.z - avstånd), int(pos.z + avstånd))
    y = random.randint(int(pos.y), int(pos.y +5))

    #skapa blocket random
    mc.setBlock(x, y, z, 20)
    
    return x,y,z
    

mc = minecraft.Minecraft.create()

mc.postToChat("kurragömma har startas!")

starttid = time.time()

pos = mc. player.getPos()

block_x, block_y, block_z = skapa_block(pos, 200)

#mc.postToChat(str(block_x) + ", " + str(block_y) + ", " + str(block_z))

tidigare_avstånd = block_avstånd (block_x, block_y, block_z, pos)

game_over = False 

# spelloop
while not game_over:
    time.sleep(1)

    pos = mc.player.getPos()

    avstånd = block_avstånd(block_x, block_y, block_z, pos)

    if tidigare_avstånd > avstånd:
        mc.postToChat("varmare...")
    elif tidigare_avstånd < avstånd:
        mc.postToChat("kallare...")

    tidigare_avstånd = avstånd

    #mc.postToChat("avstånd är " + str(avstånd))

    nuvarande_tid = time.time()

    if avstånd < 2:
        mc.postToChat("du hittade blocket!")
        game_over = True

        spelarens_tid = int(nuvarande_tid - starttid)
        mc.postToChat("din tid: " + str(spelarens_tid) + " sekunder")
