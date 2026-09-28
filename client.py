"""Merkle Mountain Range (MMR) Accumulator Engine.
100% Python Standard Library.
"""

import hashlib

class MerkleMountainRange:
    """Append-only Merkle Mountain Range (MMR) structure."""
    def __init__(self):
        self.nodes = []

    @staticmethod
    def _hash(data):
        return hashlib.sha256(data.encode("utf-8")).hexdigest()

    def append(self, leaf_data):
        h = self._hash(f"leaf:{leaf_data}")
        self.nodes.append(h)
        return h

    def get_root_peaks(self):
        return [self.nodes[-1]] if self.nodes else []
