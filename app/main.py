import sys
import os

from .src.bin.cd import cd
from .src.bin.pwd import pwd
from .src.bin.type_command import type_command
from .src.helpers.process_arguments import process_arguments
from .src.bin.run_command_external import run_command_external


def main():

    while True:
        sys.stdout.write("$ ")
        args = process_arguments(input(''))
        command = args[0]

        if command == "exit":
            exit(0)
        elif '>' in args or '1>' in args or '2>' in args:
            os.system(" ".join(args))
            continue
        elif command == "echo":
            msg = " ".join(args[1:])
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
