from typing import List
from subprocess import run

from ..helpers.print_or_write_out import PrintOrWriteOut
from .type_command import check_pathname_command


def run_command_external(args: List[str], output: PrintOrWriteOut) -> bool:
    pathname = check_pathname_command(args[0])
    if not pathname:
        return False

    result = run(args, executable=pathname, capture_output=True, text=True)

    if result.stdout:
        output.out(result.stdout)
    if result.stderr:
        output.err(result.stderr)
    return True
