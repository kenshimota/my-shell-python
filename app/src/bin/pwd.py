from ..helpers.pathname import current_pathname
from ..helpers.print_or_write_out import PrintOrWriteOut


def pwd(output: PrintOrWriteOut):
    output.out(f"{current_pathname()}\n")
