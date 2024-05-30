import os

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
    while True:
        full_command = input("$ ")
        command_array = full_command.split()
        command = command_array[0]
        if command == "exit":
            break
        elif command == "echo":
            print(' '.join(command_array[1:]))
        elif command == "type":
            shell_type(evaled_command=str(command_array[1])) 
        elif command == "pwd":
            print(os.getcwd())
        else:
            found = False
            if os.path.exists(f"{command}"):
                os.system(f"{command} {' '.join(command_array[1:])}")
                found = True
            if not found:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
