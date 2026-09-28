# Merkle Mountain Range (MMR) Accumulator Skill

Robust, zero-dependency Python implementation of **Merkle Mountain Ranges (MMR)** for append-only verifiable ledgers and light-client consensus.

## Features
- **Append-Only History**: Adds new transaction leaves in \(O(1)\) amortized hashing time.
- **Logarithmic Inclusion Proofs**: Verifies leaf membership via peak bag roots in \(O(\log N)\) proof bytes.
- **Zero External Dependencies**: Pure Python standard library (`hashlib`).
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph TD
    L1["Leaf 1"] & L2["Leaf 2"] --> P1["Peak 1 (Height 1)"]
    L3["Leaf 3"] & L4["Leaf 4"] --> P2["Peak 2 (Height 1)"]
    P1 & P2 --> RootPeak["Mountain Peak Root (Height 2)"]
    L5["Leaf 5"] --> SinglePeak["Isolated Peak 3"]
```
