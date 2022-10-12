#coding:utf-8
# coded by geekNoe
# Nom du programme: Pandu-Game
# version : v0.01
# Descirption:
"""
    C'est un jeux permettant de joeux au pandu comme dans la vie réel
"""
#
#================================================

import os, time
from core.source import *
from core.gameLogics import *
from core.couleur import *

#================================================
def main():
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
    if (choix == "1"):
        word = pd.choiceWord()
        pd.gameLoop(word, list_pandu)
    elif (choix == "2"):
        Help()
    elif (choix == "?"):
        about()
    elif (choix == "Q" or choix == "q"):
        quit()
    else:
        print(f""*3, f"{rouge}\tVotre Choix est mauvaise !")
        time.sleep(2)
        main()

# lencement du programme
if __name__ == "__main__":
    messageBienvenue()
    main()
