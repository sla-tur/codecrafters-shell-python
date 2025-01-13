import sys

def main():
    # Uncomment this block to pass the first stage
    commands = {"exit", "echo"}
    
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        args = cmd.split()
        try:
            if args[0] not in commands:
                print(f"{args[0]}: command not found")
                continue
            else:
                match args:
                    case ["exit", "0"]:
                        exit()
                    case ["echo", *pos_args]:
                        print(*pos_args)
                    case _:
                        print(f"{cmd}: command not found")
        except:
            if args[0] not in commands:
                print(f"{args[0]}: command not found")
                continue
            else:
                return 0

if __name__ == "__main__":
    main()
