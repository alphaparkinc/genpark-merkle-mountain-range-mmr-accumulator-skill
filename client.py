import hashlib

class MerkleMountainRange:
    """Append-only Merkle Mountain Range (MMR) cryptographic accumulator."""
    def __init__(self):
        self.leaves = []

    def append(self, data: str) -> dict:
        leaf_hash = hashlib.sha256(data.encode()).hexdigest()
        self.leaves.append(leaf_hash)
        return {
            "data": data,
            "leaf_hash": leaf_hash,
            "mmr_size": len(self.leaves)
        }

    def bag_peaks(self) -> str:
        if not self.leaves:
            return ""
        return hashlib.sha256("".join(self.leaves).encode()).hexdigest()
