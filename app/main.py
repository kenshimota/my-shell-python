import sys
from pathlib import Path
from typing import List

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    __package__ = "app"

from .src.bin.cd import cd
from .src.bin.pwd import pwd
from .src.bin.run_command_external import run_command_external
from .src.bin.type_command import type_command
from .src.helpers.print_or_write_out import PrintOrWriteOut
from .src.helpers.process_arguments import apply_completer, custom_input_cmd, process_arguments

def is_writteable_file(s: List[str]) -> int:
    commands = ['>', '1>', '2>', '>>', '1>>', '2>>']
    for c in commands:
        if c in s:
            return s.index(c)
    return -1


def main():

    apply_completer()

    while True:
        output = PrintOrWriteOut()
        writtable_files = []
        command_without_out = []
        sys.stdout.write("$ ")
        args = process_arguments(custom_input_cmd(''))

        if not args:
            continue

        command = args[0]

        if command == "exit":
            exit(0)

        i = is_writteable_file(args)
        command_without_out = args[:i] if i >= 0 else args
        if i >= 0:
            writtable_files = args[i:]

        output.process_args(args)
        if command == "echo":
            msg = " ".join(command_without_out[1:])
            output.out(f"{msg}\n")
            continue
        elif command == "type":
            type_command(args[1], output)
            continue
        elif command == "pwd":
            pwd(output)
            continue
        elif command == "cd":
            cd(command_without_out[1:])
            continue

        executed = run_command_external(command_without_out, output)
        if executed:
            continue

        output.err(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
