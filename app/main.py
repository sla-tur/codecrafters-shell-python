import sys

def main():
    # Uncomment this block to pass the first stage
    commands = {"exit 0"}
    
    while True:
        sys.stdout.write("$ ")
        cmd = input()
        if cmd not in commands:
            print(f"{cmd}: command not found")
            continue
        else:
            return 0

if __name__ == "__main__":
    main()
