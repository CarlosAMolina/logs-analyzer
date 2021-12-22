from typing import Iterator
import os


LOG_FILE = os.path.join(
    os.path.dirname(__file__),
    "../../../logs-parser-results/access.log",
)


class FileExtractor:
    def __init__(self, file: str):
        self._file = file

    def get_lines_in_file(self) -> Iterator[str]:
        with open(self._file, "r") as f:
            for line in f.read().splitlines():
                if len(line) != 0:
                    yield (line)
