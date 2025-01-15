import sys
import os
import subprocess

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
                #
                print(*pos_args)
            case ["type", command]:
                paths = PATH.split(os.pathsep)
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
                paths = PATH.split(os.pathsep)
                command_path = None
                for path in paths:
                    if os.path.isfile(f"{path}/{args[0]}"):
                        command_path = f"{path}/{args[0]}"
                if command_path:
                    print(subprocess.run(args, capture_output=True,
                                         text=True).stdout)
                else:
                    sys.stdout.write(f"{args[0]}: not found\n")

if __name__ == "__main__":
    main()
