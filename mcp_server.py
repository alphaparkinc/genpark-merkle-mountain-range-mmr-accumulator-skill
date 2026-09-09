import sys
import json
from client import MerkleMountainRange

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    mmr = MerkleMountainRange()
    if method == "append_and_bag":
        for item in params.get("items", []):
            mmr.append(item)
        return {"root": mmr.bag_peaks()}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
