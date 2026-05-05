import hashlib
import json
import time


def calculate_hash(block):
    data = block.copy()
    data.pop("hash", None)
    text = json.dumps(data, sort_keys=True)
    return hashlib.sha256(text.encode()).hexdigest()


def add_block(transactions):
    previous_hash = chain[-1]["hash"] if chain else "0"
    block = {
        "index": len(chain),
        "time": time.ctime(),
        "transactions": transactions,
        "previous_hash": previous_hash,
    }
    block["hash"] = calculate_hash(block)
    chain.append(block)


chain = []

add_block(["Genesis block"])
add_block(["Alice pays Bob 10", "Bob pays Charlie 5"])
add_block(["Charlie pays Dave 2"])

for block in chain:
    print("\nBlock:", block["index"])
    print("Time:", block["time"])
    print("Transaction history:", block["transactions"])
    print("Previous hash:", block["previous_hash"])
    print("Block hash:", block["hash"])
