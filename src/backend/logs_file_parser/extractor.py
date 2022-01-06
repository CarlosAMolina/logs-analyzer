from typing import Iterator, List


def extract(file: str) -> List[str]:
    return [line for line in get_lines_in_file(file)]


def get_lines_in_file(file: str) -> Iterator[str]:
    with open(file, "r") as f:
        for line in f.read().splitlines():
            if len(line) != 0:
                yield (line)
