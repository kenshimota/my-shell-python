import sys
import subprocess
from typing import List

from .src.bin.cd import cd
from .src.bin.pwd import pwd
from .src.bin.type_command import type_command
from .src.helpers.process_arguments import process_arguments, custom_input_cmd, apply_completer
from .src.bin.run_command_external import run_command_external


def is_writteable_file(s: List[str]) -> int:
    commands = ['>', '1>', '2>', '>>', '1>>', '2>>']
    for c in commands:
        if c in s:
            return s.index(c)
    return -1


def main():

    apply_completer()

    while True:
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
        if i >= 1:
            i = is_writteable_file(args)
            writtable_files = args[i:]
            command_without_out = args[:i]

        print(writtable_files)
        print(command_without_out)

        if command == "echo":
            msg = " ".join(command_without_out[1:])
            print(msg)
            continue
        elif command == "type":
            type_command(args[1])
            continue
        elif command == "pwd":
            pwd()
            continue
        elif command == "cd":
            cd(args)
            continue

        executed = run_command_external(args)
        if executed:
            continue

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
