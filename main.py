#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import *

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Matematika"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)

        self.bind("<Escape>", self.quit)

        self.lbl = tk.Label(self, text="Vypočítej:")
        self.lbl.pack()

    
        #výsledek
        self.entry = Entry(self, width = 5)
        self.entry.pack(side = RIGHT,padx= 40, pady=20)

        #=
        self.label1 = Label(self, text ="=")
        self.label1.pack(side = RIGHT)

        #příklad
        self.entry = Entry(self, width = 15)
        self.entry.pack(side = RIGHT, padx= 40, pady=20)

        #self.btn = tk.Button(self, text="Quit", command=self.quit)
        #self.btn.pack()

        self.generuj()
        


    def generuj(self):
        self.funkce = random.choice([self.plus, self.deleno, self.krat, self.minus])
        self.label = Label(self, text=1)
        

    def plus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100-self.cisloA) 
        self.vysledek = self.cisloA + self.cisloB
        self.lbl.config(text="+")

    def deleno(self):
        self.cisloA = random.randint(1, 10)
        self.vysledek =random.randint(1, 10)
        self.cisloB = self.cisloB * self.vysledek
        self.lbl.config(text="/")

    def minus(self):
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, self.cisloA) 
        self.vysledek = self.cisloA - self.cisloB
        self.lbl.config(text="-")

    def krat(self):
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10) 
        self.vysledek = self.cisloA * self.cisloB
        self.lbl.config(text="*")   

    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()