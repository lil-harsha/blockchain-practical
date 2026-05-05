import hashlib
import json


def calculate_hash(block):
    data = block.copy()
    data.pop("hash", None)
    text = json.dumps(data, sort_keys=True)
    return hashlib.sha256(text.encode()).hexdigest()


chain = []
previous_hash = "0"

for i in range(1, 6):
    block = {
        "node": i,
        "transaction": f"Transaction {i}",
        "previous_hash": previous_hash,
    }
    block["hash"] = calculate_hash(block)
    chain.append(block)
    previous_hash = block["hash"]

for block in chain:
    print("Node:", block["node"])
    print("Block hash:", block["hash"])
    print()
