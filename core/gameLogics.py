#!/bin/env/python3


__author__ = "Coded by N30-Geek"
__name___  = "Pandu Gamr"
__version__ = "python3.9"

"""
	Ce Jeux est la version en console du jeux de pandu
	coder par Geek Néo...
	
	Dans ce code se trouve l'ensemble de logiques du jeux
	La classe principale appelle Pandu et quelques fonction
"""

#Les modules utilisers

import time, os
from random import randint

def word_fanct(file_name):
    # La fonction qui prend un fichier en paramettre et return
    # un mot dedans aleatoirement 
    list_word =    []
    words = open(file_name, 'r')
    for w in words:
        list_word.append(w)
    return list_word[randint(0, len(list_word)-1)]
#==================================================
# La classe principale du logique du jeux 
#==================================================

class Pandu:
    
    def __init__(self, word):
        self.word_found = []
        self.word =  word
        self.lenWord = len(self.word)
        self.life = len(self.word)
        self.underscoreWord = []

    def startgame(self):
        self.compAjoutUnderscore = 1     
        self.indexListe = []    # liste des indexs des caractères présent dans les mots 
        self.life = 8           # la variable qui contient la vie du jeux
        while self.compAjoutUnderscore < len(self.word):
            self.underscoreWord.append("_")
            if self.compAjoutUnderscore == len(self.word):
                break
            self.compAjoutUnderscore += 1
        
        self.looping = 0 # les compteur de la boucle principale du jeux
        while self.looping <= self.lenWord:
            print()
            self.space = " "*12
            for self.i in self.underscoreWord:
                print(self.i + " ", end="")
            print("\n\n")
            print("="*50)
            self.wordSuggested = input("\n\nEntrer la lettre suggere : ")
            if(self.wordSuggested == self.word[self.looping]):
                for self.c in self.word:
                    if (self.c == self.wordSuggested):
                        self.indexListe.append(self.word.index(self.c))
                print(self.indexListe)
                print("Votre vie est de encore [", self.life, " ]")
                self.looping += 1
            else:
                self.life -= 1
                print("Tu n'a pas trouver le bon mots")
                print("Il vous reste ", self.life, " vie à gèré")
                self.looping += 1
                
                
# MENU PRINCIPALE

if __name__ == "__main__":
    output = word_fanct("WordsList.neo")
    pd = Pandu(output)
    print(output)
    print()
    print("="*50)
    pd.startgame()