import sys

def main():
    # Uncomment this block to pass the first stage
    commands = {"exit", "echo"}
    #
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        args = cmd.split()
        try:
            if args[0] not in commands:
                print(f"{args[0]}: command not found")
                continue
            else:
                if args[0] == 'exit':
                    try:
                        return int(args[1])
                    except:
                        print(f"{cmd}: command not found")
                        continue
                elif args[0] == 'echo':
                    print(" ".join(args[1:]))
        except:
            if args[0] not in commands:
                print(f"{args[0]}: command not found")
                continue
            else:
                return 0

if __name__ == "__main__":
    main()
