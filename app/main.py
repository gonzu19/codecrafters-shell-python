import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    command_array = command.split()
    print(f"{command_array[0]}: command not found")


if __name__ == "__main__":
    main()
