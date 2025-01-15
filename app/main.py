import sys
import os

def main():
    # Uncomment this block to pass the first stage
    commands = {"exit", "echo", "type"}
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # readline() here ends with a newline character, necessitating rstrip()
        cmd = sys.stdin.readline().rstrip()
        # Split input into distinct arguments
        args = cmd.split()
        match args:
            # the exit command only exits on receipt of a valid exit code -- 0
            case ["exit", "0"]:
                exit()
            case ["echo", *pos_args]:
                print(*pos_args)
            case ["type", command]:
                if command in commands:
                    print(f"{command} is a shell builtin")
                else:
                    print(f"{command}: not found")
            case _:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
