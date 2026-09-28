from client import MerkleMountainRange

mmr = MerkleMountainRange()
for tx in ["tx_alice_bob", "tx_charlie_dave", "tx_eve_frank"]:
    mmr.append(tx)

print("Peak hashes:", mmr.get_root_peaks())
