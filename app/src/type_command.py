from os import environ, path, listdir

PATH_EXECUTE = {}
pathnames = environ.get("PATH", "").split(":")

for dir in pathnames:
    if not path.isdir(dir):
        continue

    files = listdir(dir)
    if not files:
        continue
    for command in files:
        PATH_EXECUTE[command] = f"{dir}/{command}"

def check_pathname_command(s: str) -> str:
    return PATH_EXECUTE.get(s, '')

def type_command(s: str):
    command_valids_without_type = set(["echo", "exit", "type"])

    if s in command_valids_without_type:
        print(f"{s} is a shell builtin")
    else:
        pathname = check_pathname_command(s)
        msg = f"{s} is {pathname}" if pathname else f"{s}: not found"
        print(msg)
