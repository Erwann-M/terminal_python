from random import randint
from command import Command

Command = Command()

class Terminal():
    
    def __init__(self):    
        self.terminal_name = "Terminal"
        self.computer_name = "Computer"
        self.host_name = "Name"
        self.password_root = "root"
        self.root = False
        self.open = True
        
        
    def input_command(self, command):
        
        # verifie s'il y a un espace entre des mots
        if " " in command:
            command = command.split(" ")
        
        
        if command == "quit" or command == "exit":
            self.open = False
            
        elif command == "help":
            if self.root:
                Command.help_root_command()
            else:
                Command.help_command()
            
        elif command == "":
            pass
        
        elif command[0] == "name":
            self.host_name = command[1]
            print("Votre nom a bien été modifier.")
            
        elif command[0] == "computer":
            self.computer_name = command[1]
            print("Le nom de votre ordinateur a bien été modifier.")
            
        elif command[0] == "terminal":
            self.terminal_name = command[1]
            print("Le nom du terminal a bien été modifier.")
            
        elif command == "su":
            if self.root == False:
                if Command.root_mode(self.password_root):
                    self.root = True
            else:
                print("Vous êtes déja en mode root...")
                print("Pour quitter le mode root tapez : \"su -r\"")
                
        elif command[0] == "su":
            if command[1] == "-r":
                self.root = False
            elif command[1] == "-pwd":
                new_password = Command.modify_root_password(self.password_root)
                if new_password != False:
                    self.password_root = new_password
            else:
                print(f"L'argument \"{command[1]}\" n'est pas reconnu pour la commande \"su\"")
                
        elif command[0] == "timer":
            input(f"Appuyez sur entrée pour lancer le timer.")
            Command.timer_command(command[1])
            
        elif command == "matrix":
            Command.matrix_command()
            
        else:
            Command.error_command(command)