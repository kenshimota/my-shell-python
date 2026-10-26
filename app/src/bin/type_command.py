from functools import lru_cache
from os import environ, path, listdir, access, X_OK

from ..helpers.print_or_write_out import PrintOrWriteOut

def check_pathname_command(s: str) -> str:
    path_env = environ.get("PATH", "")
    if not path_env:
        return ""

    for dir in path_env.split(path.pathsep):
        if not path.isdir(dir):
            continue
        full_path = path.join(dir, s)
        if path.isfile(full_path) and access(full_path, X_OK):
            return full_path

    return ''


def type_command(s: str, output: PrintOrWriteOut):
    command_valids_without_type = set(["echo", "exit", "type", "pwd", "cd"])

    if s in command_valids_without_type:
        output.out(f"{s} is a shell builtin")
    else:
        pathname = check_pathname_command(s)
        if pathname:
            output.out(f"{s}: {pathname}")
        else:
            output.err(f"{s}: not found")
