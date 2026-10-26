from os import chdir
from typing import List

from ..helpers.pathname import get_pathname_direction, is_directory


def cd(args: List[str]):
    if len(args) < 1:
        print("you have use unless 1 argument")
        return

    if len(args) > 1:
        print("there are many arguments")
        return

    pathname = get_pathname_direction(args[0])

    if not is_directory(pathname):
        print(f"cd: {pathname}: No such file or directory")
        return

    chdir(pathname)
