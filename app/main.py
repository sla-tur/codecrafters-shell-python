import sys

def main():
    # Uncomment this block to pass the first stage
    commands = {exit}

    sys.stdout.write("$ ")
    cmd = input()
    while cmd not in commands:
        print(f"{cmd}: command not found")
        sys.stdout.write("$ ")
        cmd = input()
    if cmd[0:3] == 'exit':
        return 0

if __name__ == "__main__":
    main()
