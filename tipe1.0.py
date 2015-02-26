#!/usr/bin/python3
# coding: iso-8859-1 

import os, time, sys
from msvcrt import getch
import tkinter as tk
# routeurprécédent§§§adressefinale§§§expéditeur§§§message
#      0                   1                 2         3

def url(num): return "taches\ordi"+str(num)+".py"
class Ordi :
  def __init__(self, num, region):
    self.num = num
    self.voisins = []    # creates a new empty list for each computer
    self.url = url(num)
    #os.remove(self.url) # on vire l'ancien fichier
    self.fichier = open(self.url, "w")
    self.fichier.close()
    self.table = region
  
  def envoi(self, param): # le facteur sera forcément un voisin de self
    facteur = self.table[param[1]]  # on cherche par qui il faut passer
    phrase = self.num +"§§§"+ param[1] +"§§§"+ param[2] +"§§§"+ param[3]
    f=open(url(facteur),"a")
    f.write(phrase + "\n")
    f.close()
    return True
  
  def traitement(self):
    f=open(self.url, "r")
    tache = f.readline()
    contenu = f.read()
    f.close()
    f=open(self.url, "w")
    f.write(contenu)
    f.close()
    
    param = str.split("$$$") # /!\ là c'est param[0...] et pas param['dest'...]
    if(param[1] == self.num):
      print("L'ordi "+param[2]+" vous envoie : \""+ param[3] +"\".")
      return ""
    # else:
    param[0] = self.num
    self.envoi(param)



  
numero = int(input("numéro ?"))
t = {}
for i in range (1,4):
  t[(numero+i)%4] = input("comment vas-tu vers %d " %((numero+i)%4))
ordi = Ordi(numero, t)

os.system("pause")

def ecrire():
  phrase = input("phrase ? ")
  dest = input("destinataire ?")
  ordi.envoi([ordi.num, dest, ordi.num, phrase])


class Keypress:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.root.bind('<KeyPress>', self.onKeyPress)
        self.key = ""

    def onKeyPress(self, event):
        print("keypressed")
        self.key = event.char

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return self.key


keypress = Keypress()
while 1:
  time.sleep(0.6)
  
  if keypress == 'c':
    break
  elif keypress == 'i': 
    print('info')
  else:
    print("i dont understand " + str(keypress))

def onKeyPress(e):
  print(e)  

#def onKeyPress(event):
 #   text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
 
  #print("tcon")
  #char = sys.stdin.read()
  #print("You pressed %s" % char)
  #if(char =="?????"):
  #  ecrire()"""
  
