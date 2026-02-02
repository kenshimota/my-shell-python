import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
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

        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
