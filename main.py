from terminal import Terminal

if __name__ == "__main__":
    
    new_terminal = Terminal()

    while new_terminal.open:
        
        if new_terminal.root:
            root = "#"
        else:
            root = "$"
        
        command = input(f"--{new_terminal.host_name}@{new_terminal.computer_name}[{new_terminal.terminal_name}] {root} ")
        new_terminal.input_command(command)