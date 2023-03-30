from dataclasses import dataclass
from typing import Any
import datetime as datetime
import hashlib

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()
        sha.update(data)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

# Create a test block and view the nonce and hash
block = Block("test", 1)
print(f"The original nonce is: {block.nonce}")
print(f"The original block hash is: {block.hash_block()}")

# Update the test block and view the nonce and hash
block.nonce += 1
print(f"The new nonce is now: {block.nonce}")
print(f"The new block hash is now: {block.hash_block()}")
