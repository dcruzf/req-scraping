import argparse
from pathlib import Path
import pickle

from src.async_requests import run_request_attempts

parser = argparse.ArgumentParser(
    prog="async requests",
    description="run async requests from a list of urls",
    epilog="",
)

parser.add_argument("filepath", type=Path)
parser.add_argument("--output", type=Path, default=Path("result.pkl"))
parser.add_argument("--attempts", type=int, default=1)

args = parser.parse_args()

urls_path: Path = args.filepath
output_path: Path = args.output
attempts: int = args.attempts
print(urls_path.absolute())

urls = urls_path.read_text()
urls = urls.splitlines()

if __name__ == "__main__":

    result = run_request_attempts(urls, attempts=attempts)
    with output_path.open('wb') as file:
        pickle.dump(result, file)
    print(f'Results in {output_path.name}')


