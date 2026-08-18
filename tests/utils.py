import json
from pathlib import Path

def load_data(path: Path) -> list[dict]:
    if not path.is_file():
        raise FileNotFoundError("The file does not exist: {path}")

    with open(path, "r") as file:
        return json.load(file)