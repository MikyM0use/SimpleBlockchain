from block import *
import datetime as date
import random



                    #index, timestamp, previous_hash
genesis_block = Block(0, date.datetime.now(), 0)
latest_block = genesis_block
latest_hash = 0
latest_index = 0


while True:


    latest_hash = latest_block.PoW(complexity="00000")

    latest_block.appendTransaction("alice gives "+str(random.randint(1,100))+" to bob")
    latest_block.appendTransaction("alice gives "+str(random.randint(1,100))+" to eve")
    latest_block.appendTransaction("bob gives "+str(random.randint(1,100))+" to eve")

    print(latest_block.toStr())

    latest_block = Block(latest_index, date.datetime.now(), latest_hash)
    latest_index += 1
