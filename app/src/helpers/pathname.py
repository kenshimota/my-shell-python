from os import getcwd, getenv
from os.path import isdir


def current_pathname() -> str:
    """Return the current working directory."""
    return getcwd()


def get_pathname_direction(pathname: str) -> str:
    """Resolve a pathname (supporting `~`, relative and absolute paths) to an absolute path."""
    if pathname == "~" or pathname.startswith("~/"):
        pathname = f"{getenv('HOME')}{pathname[1:]}"
    elif pathname == ".":
        pathname = current_pathname()
    elif not pathname.startswith("/"):
        pathname = f"{current_pathname()}/{pathname}"

    splitted = pathname.split("/")
    stack = []

    for s in splitted:
        if not s or s == ".":
            continue

        if s == ".." and stack:
            stack.pop()
        elif s != "..":
            stack.append(s)

    return "/" + "/".join(stack)


def is_directory(pathname: str) -> bool:
    return isdir(pathname)

