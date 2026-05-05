import hashlib
import time


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.time = time.ctime()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = (
            str(self.index)
            + self.time
            + str(self.transactions)
            + self.previous_hash
            + str(self.nonce)
        )
        return hashlib.sha256(text.encode()).hexdigest()

    def mine(self, difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [Block(0, ["Genesis block"], "0")]

    def add_block(self, transactions):
        block = Block(len(self.chain), transactions, self.chain[-1].hash)
        print("Mining block", block.index)
        block.mine(self.difficulty)
        self.chain.append(block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True


bc = Blockchain(difficulty=4)
bc.add_block(["Alice pays Bob 10"])
bc.add_block(["Bob pays Charlie 5"])

for block in bc.chain:
    print("\nBlock:", block.index)
    print("Transactions:", block.transactions)
    print("Previous hash:", block.previous_hash)
    print("Nonce:", block.nonce)
    print("Hash:", block.hash)

print("\nBlockchain valid?", bc.is_valid())
