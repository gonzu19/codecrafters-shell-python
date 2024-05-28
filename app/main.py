import sys
import os

def echo(command_array:list) -> None:
    echo = ""
    for word in command_array[1:]:
        echo += f"{word} "
        print(echo.rstrip())

def shell_type(evaled_command:str) -> None:
    if evaled_command in ["echo","exit","type"]:
        print(f"{evaled_command} is a shell builtin")
        return
    paths = os.getenv("PATH").split(":")
    for path in paths:
            if os.path.exists(f"{path}/{evaled_command}"):
                print(f"{evaled_command} is {path}/{evaled_command}")
                return
    print(f"{evaled_command} not found")


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
            echo(command_array=command_array)
        elif command == "type":
            shell_type(evaled_command=str(command_array[1])) 
        else:
            print(f"{command_array[0]}: command not found")


if __name__ == "__main__":
    main()
