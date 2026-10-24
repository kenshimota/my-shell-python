import sys
from typing import List
from subprocess import run, CalledProcessError

from .type_command import check_pathname_command


def run_command_external(args: List[str]) -> bool:
    pathname = check_pathname_command(args[0])
    if not pathname:
        return False

    output = run(" ".join(args), shell=True,  capture_output=True, text=True)

    if output.stderr:
        sys.stderr.write(output.stderr)
        return True

    sys.stdout.write(output.stdout)
    return True
