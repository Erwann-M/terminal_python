import getpass
from random import randint
import time
import winsound
import shutil


class Command():
    def __init__(self):
        self.separator = "-"
        self.frame = "="
        self.terminal_width = shutil.get_terminal_size().columns
        self.help = {
            "quit/exit": "quitter le terminal\n",
            "help": "affiche l'aide\n",
            "name": "changer le nom d'hôte\n",
            "computer": "changer le nom de l'ordinateur\n",
            "terminal": "changer le nom du terminal\n",
            "su": "mettre le terminal en root\n",
            "timer X": "Lancer un timer de X secondes\n",
            "matrix": "Essaye et tu verra ;)\n",
        }
        self.help_root = {
            "su -r": "sortir du mode root\n",
            "su -pwd": "changer le mot de passe root\n"
        }
        
    
    def error_command(self, command):
        print("")
        print(self.frame.center(50, "="))
        print(f"La commande: \"{command}\" n'est pas reconnue.".center(50, " "))
        print("Tapez \"help\" pour voir la liste des commandes".center(50, " "))
        print(self.frame.center(50, "="), "\n")
        
    def help_command(self):
        print("")
        print("HELP".center(50, "=") + "\n")
        
        for help_item in self.help:
            print(help_item + " : " + self.help[help_item])
            
        print(self.frame.center(50, "="), "\n")
        
    def root_mode(self, password):
        mdp = getpass.getpass("Veuillez entrer votre mot de passe : ")
        if mdp == password:
            print(self.frame.center(30, "="))
            print("\nMODE ROOT ACTIVÉ\n")
            print(self.frame.center(30, "="))
            return True
        else:
            print("\nMauvais mot de passe...\n")
            return False
        
    def modify_root_password(self, password):
        mdp = getpass.getpass("Veuillez entrer votre mot de passe : ")
        if mdp == password:
            print("Bon mot de passe.")
            mdp_are_not_modify = True
            while mdp_are_not_modify:
                new_mdp = getpass.getpass("Veuillez entrer un nouveau mot de passe : ")
                new_mdp2 = getpass.getpass("Veuillez retaper le mot de passe : ")
                if new_mdp == new_mdp2:
                    print("\nLe mot de passe a bien été changer.\n")
                    mdp_are_not_modify = False
                    return new_mdp
                else:
                    print("Les mots de passe ne correspondent pas...")
        else:
            print("\nMauvais mot de passe...\n")
            return False
        
    def help_root_command(self):
        print("")
        print(self.frame.center(50, "=") + "\n")
        
        for help_item in self.help:
            print(help_item + " : " + self.help[help_item])
            
        print("Commandes root".center(50, "-") + "\n")
        
        for help_root_item in self.help_root:
            print(help_root_item + " : " + self.help_root[help_root_item])
            
        print(self.frame.center(50, "="), "\n")
        
    def timer_command(self, seconds):
        second_left = int(seconds)
        
        while second_left != 0:
            print("< " + str(second_left) + " >")
            second_left -= 1
            time.sleep(1)
        
        print("\nC'EST BON !!!\n")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        print("\nC'EST BON !!!\n")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        print("\nC'EST BON !!!\n")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        
    def matrix_command(self):
        character = ["0", "1", " ", " ", " ", " ", " ", " ", " "]
        i = 0
        while i < 150:
            line_character = 0
            line = []
            if i < 3:
                maxi = 1
            elif i < 10:
                maxi = 2
            elif i < 40:
                maxi = 3
            elif i < 60:
                maxi = 4
            elif i < 80:
                maxi = 5
            elif i < 100:
                maxi = 6
            elif i < 120:
                maxi = 7
            elif i < 150:
                maxi = 8
            while line_character < self.terminal_width:
                line.append(character[randint(0, maxi)])
                line_character += 1
                
            print("".join(line))
            time.sleep(0.03)
            i += 1
            
if __name__ == "__main__":
    Command = Command()
    Command.matrix_command()