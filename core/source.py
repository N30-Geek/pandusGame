#!/bin/env/python3
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

	Ce Jeux est la version en console du jeux de pandu
	coder par Geek Néo Coolman
    Othor : Néo Coolman
    contact: @N30-Geek
    Version : 0.01 
    Licence : GNU 
    Description:

    Ce jeux fait la simulation au jeux de pandu
    ....
"""

#Les modules utilisers

import time, os
from core.couleur import *

#===========================================================

# implémentation de fonction principale du jeu
# slack edit passfile: DownloadDevTools.ir
############################################################

def loadingGame():
    pass
def messageBienvenue():
    '''
        Cette fonction se charge d'affache du messsage du bienvenue
    '''
    os.system("cls")
    message = f"""
{rouge}*****************************{jaune}********************************{reset}
        {jaune}Bienvenue dans notre jeux de pandu développer par
    Geek Néo Coolma, Alors ce jeux est fait exactement pour 
              vous Alors amisé vous bien !!!
        =============================================
        {blue}  __,  _, _, _ __, _,_  _,    _,  _, _, _ __,
         |_) /_\ |\ | | \ | | (_    / _ /_\ |\/| |_ 
         |   | | | \| |_/ | | , )   \ / | | |  | |  
         ~   ~ ~ ~  ~ ~   `~'  ~     ~  ~ ~ ~  ~ ~~~{jaune}

        C'est jeux est en open-source, dont vous pouvez le 
                Modifier comme bon vous semble
                ----------------------------
                    {verte}mon github: N30-Geek {reset}
{rouge}*****************************{jaune}********************************{reset}      
    """
    for m in message:
        print(m, end="")
    os.system("pause")
    os.system("cls")
def arbreEtChoix():
    print(" ________.__")
    print("  Y      {}\t\tMenu principal".format("|")) 
    print("  |      {}\t\t============".format("O"))
    print("  |     {}\t\t*[!] --[P] Play".format("/Π\\"))
    print("  |      {}\t\t*[!] --[?] Help ?".format("="))
    print("  |     {}\t\t*[!] --[A] About".format("/ \\"))
    print("  |       \t\t*[*] --[Q] Exit")
    print("  | ")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")

##==== les fonction princiaple de 

def perd0():
    print(" __________")
    print("  Y")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd1():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd2():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd3():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |      {}".format("Π"))
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd4():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |     {}".format("/Π"))
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd5():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |     {}".format("/Π\\"))
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd6():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |     {}".format("/Π\\"))
    print("  |      {}".format("="))
    print("  |")
    print("  |")
    print("  |")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd7():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |     {}".format("/Π\\"))
    print("  |      {}".format("="))
    print("  |     {}".format("/ "))
    print("  | ")
    print("  | ")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
def perd8():
    print(" __________")
    print("  Y      {}".format("|"))
    print("  |      {}".format("O"))
    print("  |     {}".format("/Π\\"))
    print("  |      {}".format("="))
    print("  |     {}".format("/ \\"))
    print("  | ")
    print("  | ")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")
    
# La fonction du masquage du word dans le fichier

logo=""" 
   __,  _, _, _ __, _,_  _,    _,  _, _, _ __,
   |_) /_\ |\ | | \ | | (_    / _ /_\ |\/| |_ 
   |   | | | \| |_/ | | , )   \ / | | |  | |  
   ~   ~ ~ ~  ~ ~   `~'  ~     ~  ~ ~ ~  ~ ~~~
   """
def main(logo):
    print(logo)
    print("   Jouer à ce Jeux de pandus En mofe Console")
    arbre()

def quit():
    os.system("cls")
    messageGo = f"""{verte}    
        Merci d'avoir joué avec nous ce jeux alors
    {rouge}         --------------------------------
              {blue}   ---- BYE BYE ): ---- {reset}
                    """
    for i in messageGo:
        print(i, end="")
    time.sleep(5)
    os.system("cls")
    os.system("exit")
def help(file_name, textEdit):
    os.system(textEdit +"core/"+file_name)
def about():
    os.system("cls")
    print(f"""

       {verte} Jeux de pandu version : v.0.1
        -----------------------------
        Développer par : N30-Geek
        Version du jeux : v0.1
        Licence : GNU Linux (open Source)
        PlanteForme : Wn32
        *****************************
    Github  : https://www.github.com/N30-Geek
    facebook: incaming
    Youtube : incoming
    SoloLearn : incoming
    ---------------------------------------
        Notre jeux est encour de développer
        l*********************************l
    """)
    os.system("pause")