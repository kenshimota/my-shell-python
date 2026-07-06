import sys

from .src.pwd import pwd
from .src.type_command import type_command
from .src.run_command_external import run_command_external


def main():

    while True:
        sys.stdout.write("$ ")
        command = input()
        args = command.strip().split(" ")
        command = args[0]

        if command == "exit":
            exit(0)
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

        executed = run_command_external(args)
        if executed:
            continue

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
