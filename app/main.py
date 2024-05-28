import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        full_command = input()
        command_array = full_command.split()
        command = command_array[0]
        if command == "exit":
            break
        elif command == "echo":
            echo = ""
            for word in command_array[1:]:
                echo += f"{word} "
            print(echo.rstrip())
        else:
            print(f"{command_array[0]}: command not found")


if __name__ == "__main__":
    main()
