#coding:utf-8
"""
 ███▄    █  ▄████▄  
 ██ ▀█   █ ▒██▀ ▀█  
▓██  ▀█ ██▒▒▓█    ▄  Pandu v0.01
▓██▒  ▐▌██▒▒▓▓▄ ▄██▒ N30-Geek
▒██░   ▓██░▒ ▓███▀ ░ 
░ ▒░   ▒ ▒ ░ ░▒ ▒  ░
░ ░░   ░ ▒░  ░  ▒   
   ░   ░ ░ ░        
         ░ ░ ░      
           ░ 
    
    Ce script contient les codes principale d'appel 
    des du lencement et d'appelle de toutes les fonctions et méthode du jeux.
"""
#
#================================================

import os, time, sys
from core.source import *
from core.gameLogics import *
from core.couleur import *

#================================================
def main():
    while True:
        os.system("cls")
        file_name = "core/wordsList.neo"
        pd = Pandu(file_name)
        list_pandu = [
            perd1,
            perd2,
            perd3,
            perd4,
            perd5,
            perd6,
            perd7,
            perd8
        ]
        logo=f""" 
           {rouge} __,  _, _, _ __, _,_  _,    _,  _, _, _ __,
            {blue}|_) /_\ |\ | | \ | | (_    / _ /_\ |\/| |_ 
            {blue}|   | | | \| |_/ | | , )   \ / | | |  | |  
            {rouge}~   ~ ~ ~  ~ ~   `~'  ~     ~  ~ ~ ~  ~ ~~~{reset}
                    >>>  Le jeux de pandu   <<<
            """
        print(logo)
        arbreEtChoix()
        choix = input(f"\t{blue}Votre choix ici >>>>{jaune} ")
        if (choix == "p" or choix == "P"):
            word = pd.choiceWord()
            pd.gameLoop(word, list_pandu)
        elif (choix == "?"):
            if(sys.platform == "win32"):
                help("help_file.help", 'notepad')
            if(sys.platform == "linux"):
                help("help_file.help", 'cat ')
        elif (choix == "a" or choix == "A"):
            about()
        elif (choix == "Q" or choix == "q"):
            quit()
            break
        else:
            print(f""*3, f"{rouge}\tVotre Choix est mauvaise !")
            time.sleep(2)


# lencement du programme
if __name__ == "__main__":
    messageBienvenue()
    main()
