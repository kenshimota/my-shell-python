from typing import List
from subprocess import run, CalledProcessError

from .type_command import check_pathname_command


def run_command_external(args: List[str]) -> bool:
    try:
        pathname = check_pathname_command(args[0])
        if not pathname:
            return False

        output = run(args, capture_output=True, check=True)
        out = output.stdout.decode().strip()
        print(out)
        return True

    except CalledProcessError as e:
        print(f"the process was a error {e}")
        return True
