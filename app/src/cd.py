from os import chdir, getenv
from os.path import isdir
from typing import List

from .pwd import current_pathname


def cd(args: List[str]):
    if len(args) < 2:
        print("you have use unless 2 arguments")
        return

    if len(args) > 2:
        print("there are many arguments")
        return

    pathname = args[1]
    if pathname[0] == "~":
        pathname = f"{getenv("HOME")}{pathname[1:]}"
    elif (pathname[0] != "~" and pathname[0] != "/") or pathname == ".":
        pathname = f"{current_pathname()}/{pathname}"

    splitted = pathname.split('/')
    stack = []

    for s in splitted:
        if not s or s == '.':
            continue

        if s == '..' and stack:
            stack.pop()
        elif s != '..':
            stack.append(s)

    pathname = "/".join(stack)
    pathname = f"/{pathname}"

    if not isdir(pathname):
        print(f"cd: {pathname}: No such file or directory")
        return

    chdir(pathname)
