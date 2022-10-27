#coding:utf-8
# coded by geekNoe
# Nom du programme: Pandu-Game
# version : v0.01
# Descirption:
"""
    C'est un jeux permettant de joeux au pandu comme dans la vie réel
"""
#================================================

import os, time
import colorama as color
from random import choice
from core.source import *

#================================================

class Pandu:
    """
        Nom de la classe : Pandu
        Methode:
            * 
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.word_list = []
        with open(self.file_name, "r") as file:
            for self.w in file:
                self.word_list.append(self.w)
  
    def choiceWord(self):
        """
            Cette methode return un mot seulectionne aléatoirement
            paramettre : None
            return : word
        """
        return choice(self.word_list)
        
    def gameLoop(self, word, list_pandu):
        self.word = word
        self.list_pandu = list_pandu
        self.length_list_pandu = len(list_pandu)
        self.view = list("_"*len(self.word[:-1]))
        self.life = 8
        while self.life > 0:
            os.system("cls")
            print(logo)
            print(f"{blue}:"*50)
            print(f"{verte}*"*50)
            print(f" {rouge} ---{blue} Vous êtes en mode play et bonne change{rouge} ---{reset}")
            print(f' {jaune} --- Nombre de vie : {rouge}[{self.life}]{jaune}')

            if(self.life == 8):
                perd0()
            if(self.life == 7):
                perd1()
            if(self.life == 6):
                perd2()
            if(self.life == 5):
                perd3()
            if(self.life == 4):
                perd4()
            if(self.life == 3):
                perd5()
            if(self.life == 2):
                perd6()
            if(self.life == 1):
                perd7()
            if(self.life == 0):
                perd8()
            # time.sleep(5)
            self.indice = []
            self.word_found = []
            self.comp = 0
            print(f"\n\t {' '.join(self.view).upper()}")
            self.proposition = input(f"\t\n{verte}Proposer une lettre >>{jaune} ")
            if(self.proposition != "" and self.proposition in self.word):
                time.sleep(0.2)
                print(f"\t{blue} --- HoooKays! Cool bien vue --- ")
                while self.comp <= len(self.word)-1:
                    if (self.word[self.comp] == self.proposition):
                        self.word_found.append(self.word[self.comp])
                        self.indice.append(self.comp)
                        self.comp += 1
                    else:
                        self.comp += 1
                        pass
                    if self.comp == len(self.word)-1:
                        break
                self.temp = 0
                for self.v in self.indice:
                    self.view[self.v] = self.word_found[self.temp]
                    self.temp += 1
            else:
                self.life -= 1
                print()
                time.sleep(0.2)
                print(f"\t{rouge} Ooops! Noops! Raté vous avez perdu un point")
                if (self.life == 0):
                    print("Vous êtes en cours de vie !")
                    print("Vous avez perdu la partie peut-être la  prochaine fois!")
                    print("Nous nous trouvons ici avec joel")
                    os.system("pause")
                    break
            if ("_" not in self.view):
                print(f"{blue} --- Victoire vous avez gagner le jeux esseyez \n --- le mot étais bien : {jaune}[{self.word.upper()}]")
                os.system("pause")
                break

# if __name__ == "__main__":
#     file_name = "core/wordsList.neo"
#     pd = Pandu(file_name)
    