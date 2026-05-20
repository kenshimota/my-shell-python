from os import environ, path, listdir, access, X_OK

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

def type_command(s: str):
    command_valids_without_type = set(["echo", "exit", "type"])

    if s in command_valids_without_type:
        print(f"{s} is a shell builtin")
    else:
        pathname = check_pathname_command(s)
        msg = f"{s} is {pathname}" if pathname else f"{s}: not found"
        print(msg)
