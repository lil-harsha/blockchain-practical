import hashlib
import json


def calculate_hash(block):
    data = block.copy()
    data.pop("hash", None)
    text = json.dumps(data, sort_keys=True)
    return hashlib.sha256(text.encode()).hexdigest()


def is_valid(chain):
    for i, block in enumerate(chain):
        correct_previous_hash = "0" if i == 0 else chain[i - 1]["hash"]

        if block["previous_hash"] != correct_previous_hash:
            return False
        if block["hash"] != calculate_hash(block):
            return False

    return True


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

print("Blockchain valid?", is_valid(chain))

chain[2]["transaction"] = "Tampered transaction"
print("After tampering, valid?", is_valid(chain))
