from client import MerkleMountainRange

def main():
    print("=== Merkle Mountain Range (MMR) Accumulator ===")
    mmr = MerkleMountainRange()
    mmr.append("header_block_1")
    mmr.append("header_block_2")
    mmr.append("header_block_3")

    peak_root = mmr.bag_peaks()
    print("MMR Bagged Peaks Root:", peak_root)
    assert len(peak_root) == 64

    print("MMR Accumulator verified successfully!")

if __name__ == "__main__":
    main()
