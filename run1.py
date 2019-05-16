from block import *
import datetime as date



                    #index, timestamp, previous_hash
genesis_block = Block(0, date.datetime.now(), 0)

genesis_block.appendTransaction("alice gives 10 to bob")
genesis_block.appendTransaction("alice gives 5 to eve")
genesis_block.appendTransaction("bob gives 1 to eve")

print(genesis_block.hash_block())
