import argparse
from pathlib import Path
from src.async_requests import chunk_requests


parser = argparse.ArgumentParser(
    prog="async requests",
    description="run async requests from a list of urls",
    epilog="",
)

parser.add_argument("filepath", type=Path)
parser.add_argument("--chunk", type=int)
parser.add_argument("--end", type=int)
parser.add_argument("--start", type=int)
args = parser.parse_args()

path = args.filepath
chunksize = args.chunk or 10
end_url = args.end
start_url = args.start

urls = path.read_text()
urls = urls.splitlines()

if __name__ == "__main__":

    print("path: ", path)
    print("chunksize: ", chunksize)

    result = chunk_requests(urls[start_url:end_url], chunksize=chunksize)
    describe = {}
    result200 = []
    for response in result:
        describe[response.status_code] = 1 + describe.get(
            response.status_code, 0
        )
        if response.status_code == 200:
            result200.append(response)

    print(*describe.keys())
    print(*describe.values())
