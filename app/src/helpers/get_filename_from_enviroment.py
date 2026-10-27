from os import environ, scandir, access, path, X_OK


def get_command_from_enviroment() -> set:
    execute_files = {"cd", "echo", "exit", "pwd", "type"}

    path_env = environ.get("PATH", "")
    if not path_env:
        return execute_files

    for dir in path_env.split(path.pathsep):
        if not path.isdir(dir):
            continue

        with scandir(dir) as entries:
            for entry in entries:
                if not path.isfile(entry):
                    continue
                if not access(entry, X_OK):
                    continue
                execute_files.add(entry.name)

    return execute_files
