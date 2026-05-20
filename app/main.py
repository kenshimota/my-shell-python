import sys
from .src.type_command import type_command

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


        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
