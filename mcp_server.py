import sys
import json
from client import MerkleMountainRange

mmr = MerkleMountainRange()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "mmr_append",
                        "description": "Append leaf element to Merkle Mountain Range and query mountain peaks",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "leaf": {"type": "string"}
                            },
                            "required": ["leaf"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "mmr_append":
            h = mmr.append(args["leaf"])
            peaks = mmr.get_root_peaks()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"leaf_hash": h, "peaks": peaks, "total_nodes": len(mmr.nodes)})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
