import tkinter as tk
from tkinter import *
import sys
import time
import os
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from hashlib import sha256
filesave = ""
entree = ""
sortie = ""
a = ""
indexshowcle = "cacher"
btncle = "Cacher la clé"
i = 0
entrycle = 0
writefile = ""
slashcounter = 0
end = ""
file2 = ""
readfile = ""
inverswritefile = ""
openinvers = ""
readinvers = ""
root = Tk()
root.geometry("1160x567")
root.maxsize(1160,567)
root.minsize(1160,567)
root.title("ZXnotes - Editeur de texte sécurisé") 
root.config(bg="#111111", padx = 0, pady = 0)


E1 = tk.Text(root, bd =5)
E1.config(borderwidth=0 , font=("Calibri", 16), width=102,   bg="#3A3A3A", selectbackground="#8A2626", fg="#D3D3D3",padx= 10)
E1.place(height=500, x = 9, y= 40)

def chiffrement():
	global key
	global entree
	global sortie
	global end
	global file2
	global readfile

	file2 = open("user\\temporary\\Temporary.txt", "r")
	readfile = file2.read()
	file2.close()
	while len(readfile) < 1:
		print("wait")
		file2 = open("user\\temporary\\Temporary.txt", "r")
		readfile = file2.read()
		file2.close()
	key = E2.get()
	keys = sha256(key.encode('utf-8')).digest()
	print("ok1")
	with open(entree, 'rb') as f_entree:
		print("ok2")
		with open(sortie, 'wb') as f_sortie:
			print("ok3")
			i = 0
			while f_entree.peek():
				print("chiffrement")
				c = ord(f_entree.read(1))
				j = i % len(keys)
				b = bytes([c^keys[j]])
				f_sortie.write(b)
				i = i + 1
			file2 = open("user\\temporary\\Temporary.txt", "w+")
			file2.truncate(0)
			file2.close()
			print("chiffrement complet")





def ily():
	global a
	global entree
	global sortie
	global filesave
	global i
	global file2
	slashcounter = 0
	a = E1.get("1.0",'end-1c')
	file2 = open("user\\temporary\\Temporary.txt", "w+")
	file2.write(a)
	file2.close()
	print("file written")
	entree = "user\\temporary\\Temporary.txt"
	files = [('Text Document', '*.txt')]
	filesave = asksaveasfile(filetypes = files, defaultextension = files)
	writefile = filesave.name
	sortie = filesave.name
	chiffrement()

	


def effacer():
	E1.delete(1.0, END)

def dechiffrement():
	global inverswritefile
	global filename
	global openinvers
	global readinvers
	print(E2.get())
	if len(E2.get()) > 0 and E2.get() != " Pour chiffrer / déchiffrer , insérez votre clé privée":
		filename = askopenfilename()
		print(filename)
		inverswritefile = filename
		openinvers = open(inverswritefile, "r+")
		readinvers = openinvers.read()
		openinvers.close()
		openinvers = open("user\\temporary\\Temporary.txt", "w+")
		openinvers.write(readinvers)
		openinvers.close()
		entree = "user\\temporary\\Temporary.txt"
		sortie = inverswritefile
		key = E2.get()
		keys = sha256(key.encode('utf-8')).digest()
		print("ok1")
		with open(entree, 'rb') as f_entree:
			print("ok2")
			with open(sortie, 'wb') as f_sortie:
				print("ok3")
				i = 0
				while f_entree.peek():
					print("chiffrement")
					c = ord(f_entree.read(1))
					j = i % len(keys)
					b = bytes([c^keys[j]])
					f_sortie.write(b)
					i = i + 1
				openinvers = open("user\\temporary\\Temporary.txt", "w+")
				openinvers.truncate(0)
				openinvers.close()
				print("chiffrement complet")



	

def click(*args):
	global entrycle
	if entrycle < 1:
		E2.delete(0, END)
		entrycle +=1

def showkey():
	global i
	global indexshowcle
	if len(E2.get()) > 0 :
		i = 0
		print(indexshowcle)
		if indexshowcle == "cacher":
			E2.config(show="ﾒ")
			indexshowcle = "afficher"
			i = 1
			Btn3.config(text="Afficher la clé")

		if indexshowcle == "afficher" and i == 0:
			E2.config(show="")
			indexshowcle = "cacher"
			Btn3.config(text="Cacher la clé")







Btn = tk.Button(text="Chiffrer et Sauvegarder", command = ily)
Btn.config(width=20, font=("Calibri", 12), bg="#1B1B1B", borderwidth=0, fg="white")
Btn.pack()
Btn.place(x = 0, y = 5, height=30)

Btn2 = tk.Button(text="Déchiffrer un fichier", command = dechiffrement)
Btn2.config(width=20, font=("Calibri", 12), bg="#1B1B1B", borderwidth=0, fg="white")
Btn2.pack()
Btn2.place(x = 170, y = 5, height=30)

Btn2 = tk.Button(text="Tout effacer", command = effacer)
Btn2.config(width=20, font=("Calibri", 12), bg="#1B1B1B", borderwidth=0, fg="white")
Btn2.pack()
Btn2.place(x = 340, y = 5, height=30)

E2= Entry(root, bd =5)
E2.config(borderwidth=0 , font=("Calibri", 12))
E2.pack()
E2.place(x= 680, y = 5, width=476, height=30)
E2.config(show="", bg="#3A3A3A", fg="#D3D3D3", justify=CENTER);
E2.insert(0, " Pour chiffrer / déchiffrer , insérez votre clé privée")
E2.bind("<Button-1>", click)


Btn3 = tk.Button(text=btncle, command = showkey)
Btn3.config(width=20, font=("Calibri", 12), bg="#1B1B1B", borderwidth=0, fg="white")
Btn3.pack()
Btn3.place(x = 510, y = 5, height=30)

root.mainloop()