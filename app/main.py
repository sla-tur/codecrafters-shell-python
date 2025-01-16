import sys
import os
import subprocess

PATH = os.environ.get("PATH")
paths = PATH.split(os.pathsep)
commands = {"exit", "echo", "type"}

def echo(*args):
    print(*args)

def type(command):
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

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # readline() here ends with a newline character, necessitating rstrip()
        cmd = sys.stdin.readline().rstrip()
        # split input into distinct arguments
        args = cmd.split()
        match args:
            # the exit command defaults to a 0 code
            case ["exit", "0"]:
                sys.exit(int(args[1]) if len(args) > 1 else 0)
            case ["echo", *pos_args]:
                echo(*pos_args)
            case ["type", command]:
                type(command)
            case _:
                paths = PATH.split(os.pathsep)
                command_path = None
                for path in paths:
                    if os.path.isfile(f"{path}/{args[0]}"):
                        command_path = f"{path}/{args[0]}"
                if command_path:
                    subprocess.run(args)
                else:
                    sys.stdout.write(f"{args[0]}: not found\n")
                sys.stdout.flush()

if __name__ == "__main__":
    main()