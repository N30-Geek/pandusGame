#!/bin/env/python3


__author__ = "Coded by N30-Geek"
__name___  = "Pandu Gamr"
__version__ = "python3.9"

"""
	Ce Jeux est la version en console du jeux de pandu
	coder par Geek Néo...

    Othor : Néo Coolman
    contact: @N30-Geek
    Version : 0.1
    
    Description:

    Ce jeux fait la simulation au jeux de pandu
    ....
"""

#Les modules utilisers

import time, os
from  gameLogics import *

#===========================================================

# implémentation de fonction principale du jeu

############################################################

def arbre():
    print(" ________.__")
    print("  Y      {}\t\tMenu principal".format("|")) 
    print("  |      {}\t\t============".format("O"))
    print("  |     {}\t\t*[▶️] --[1] Play".format("/Π\\"))
    print("  |      {}\t\t*[🆘]--[2] Help ?".format("="))
    print("  |     {}\t\t*[ℹ️] --[?] About".format("/ \\"))
    print("  |       \t\t*[🔚]--[Q] Exit")
    print("  | ")
    print(" ×Π×……°•`…`…~××•°…„„")
    print("")

##==== les fonction princiaple de 

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
   
   #
    print(logo)
    print("   Jouer à ce Jeux de pandus En mofe Console")
    arbre()

if __name__ == "__main__":
    main(logo)

    perd1()
    perd2()
    perd3()
    perd4()
    perd5()
    perd6()
    perd7()
    perd8()


    
    
    
