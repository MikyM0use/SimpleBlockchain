import hashlib
import time

class Block:
  def __init__(self, index, timestamp, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.transactions = []
    self.previous_hash = previous_hash
    self.seed = 0

  def appendTransaction(self, transaction):
      self.transactions.append(transaction)

  def PoW(self, complexity="0000"):
      start = time. time()

      while not self.hash_block().endswith(complexity):
          self.seed += 1
      print(self.seed)

      end = time. time()
      print("elapsed time: " + str(end - start))
      return self.hash_block()

  def toStr(self):
      _str= "[" + str(self.index) +"] " + str(self.timestamp) + "\n "\
                + "\tprevious hash: " + str(self.previous_hash) +\
                "\n\tcurrent hash: "+ str(self.hash) +\
                "\n\n\tseed: "+ str(self.seed)+\
                " \ntransactions: \n"

      for s in self.transactions:
          _str += "\t" + s + "\n"

      return _str

  def hash_block(self):

    self.hash = hashlib.sha256(str(self.index).encode('utf-8') +
                            str(self.timestamp).encode('utf-8') +
                            str(self.transactions).encode('utf-8') +
                            str(self.previous_hash).encode('utf-8') +
                            str(self.seed).encode('utf-8')
                            ).hexdigest()
    return self.hash
