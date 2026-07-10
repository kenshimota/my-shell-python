from typing import List
from shlex import split


def process_arguments(s: str) -> List[str]:
    s = s.strip()
    return split(s)
