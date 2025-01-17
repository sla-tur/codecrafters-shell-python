import sys
import os
import shlex
import subprocess

PATH = os.environ.get("PATH")
# os.pathsep contains the system-specific PATH separator
# (: on Unix, ; on Windows)
paths = PATH.split(os.pathsep)
commands = {"exit", "echo", "type", "pwd", "cd"}

def echo(args):
    sys.stdout.write(f"{" ".join(args)}\n")
    sys.stdout.flush()

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
        sys.stderr.write(f"{command}: not found\n")
    sys.stdout.flush()

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # readline() here ends with a newline character, necessitating rstrip()
        cmd = sys.stdin.readline().rstrip()
        # split input into distinct arguments using shlex
        args = shlex.split(cmd)
        original_stdout = sys.stdout  # Save the original stdout
        original_stderr = sys.stderr  # Save the original stderr
        if len(args) > 2 and args[-2] == "2>>":
            try:
                sys.stderr = open(args[-1], "a")  # Redirect stderr to file
                args = args[:-2]  # Remove the redirection part from args
            except Exception as e:
                sys.stderr = original_stderr
        elif len(args) > 2 and (args[-2] == "1>>" or args[-2] == ">>"):
            try:
                sys.stdout = open(args[-1], "a")  # Redirect stdout to file
                args = args[:-2]  # Remove the redirection part from args
            except Exception as e:
                sys.stdout = original_stdout
        elif len(args) > 2 and args[-2] == "2>":
            try:
                sys.stderr = open(args[-1], "w")  # Redirect stderr to file
                args = args[:-2]  # Remove the redirection part from args
            except Exception as e:
                sys.stderr = original_stderr
        elif len(args) > 2 and (args[-2] == "1>" or args[-2] == ">"):
            try:
                sys.stdout = open(args[-1], "w")  # Redirect stdout to file
                args = args[:-2]  # Remove the redirection part from args
            except Exception as e:
                sys.stdout = original_stdout  # Restore original stdout
                sys.stderr.write(f"Error: {e}\n")
                sys.stdout.flush()
                continue
        try:
            match args:
                # the exit command defaults to a 0 code
                case ["exit", "0"]:
                    sys.exit(int(args[1]) if len(args) > 1 else 0)
                case ["echo", *pos_args]:
                    echo(pos_args)
                case ["type", command]:
                    type(command)
                case ["pwd"]:
                    sys.stdout.write(f"{os.getcwd()}\n")
                    sys.stdout.flush()
                case ["cd", path]:
                    try:
                        os.chdir(os.path.expanduser(path))
                    except FileNotFoundError:
                        sys.stderr.write(f"cd: {path}: No such file or directory\n")
                        sys.stdout.flush()
                case _:
                    paths = PATH.split(os.pathsep)
                    command_path = None
                    for path in paths:
                        if os.path.isfile(f"{path}/{args[0]}"):
                            command_path = f"{path}/{args[0]}"
                    if command_path:
                        subprocess.run(args, stdout=sys.stdout, stderr=sys.stderr)  # Use redirected stdout and stderr
                    else:
                        sys.stderr.write(f"{args[0]}: not found\n")
                    sys.stdout.flush()
        finally:
            if sys.stdout != original_stdout:
                sys.stdout.close()  # Close the file if stdout was redirected
            sys.stdout = original_stdout  # Restore original stdout
            if sys.stderr != original_stderr:
                sys.stderr.close()  # Close the file if stderr was redirected
            sys.stderr = original_stderr  # Restore original stderr

if __name__ == "__main__":
    main()