import sys
import os

def main():
    # Uncomment this block to pass the first stage
    PATH = os.environ.get("PATH")
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
                sys.stdout.write(" ".join(*pos_args))
                sys.stdout.write('\n')  
            case ["type", command]:
                paths = PATH.split(":")
                command_path = None
                for path in paths:
                    if os.path.isfile(f"{path}/{command}"):
                        command_path = f"{path}/{command}"
                if command in commands:
                    sys.stdout.write(f"{command} is a shell builtin\n")
                elif command_path:
                    sys.stdout.write(f"{command} is {command_path}\n")
                else:
                    sys.stdout.write(f"{command}: not found\n")
                sys.stdout.flush()
            case _:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
