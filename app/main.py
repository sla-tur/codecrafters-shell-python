import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    cmd = input()
    while cmd:
        print(f"{cmd}: command not found")
        cmd = input()

if __name__ == "__main__":
    main()
