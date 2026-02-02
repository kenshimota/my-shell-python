import sys




def main():
    command_valids_without_type = set(["echo", "exit"])

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
        elif command == "type":
            if args[1] in command_valids_without_type:
                print(f"{args[1]} is a shell builtin")
                continue
            else:
                command = args[1]


        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
