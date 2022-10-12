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
        self.list_pandu.reverse()
        self.length_list_pandu = len(list_pandu)
        self.view = list()
        self.word_found = []
        self.life = 8

        while self.life > 0:
            print(f"\n\tMot à déviner : {self.view} ")
            self.proposition = input("\tProposer une lettre >> ")
            if(self.proposition in self.word):
                self.word += self.proposition
                print("\t --- Hooo! Cool bien vue --- ")
                self.view =""
            else:
                self.life -= 1
                self.length_list_pandu -= 1
                print("\t Ooops! Noops! Raté vous avez perdu un point")
                self.list_pandu[self.length_list_pandu]
                if (self.life == 0):
                    break
            print(self.word_found)
            for self.c in self.word:
                if (self.c in self.word_found):
                    self.view += self.c + " "
                else:
                    self.view += "_ "



# if __name__ == "__main__":
#     file_name = "core/wordsList.neo"
#     pd = Pandu(file_name)
    