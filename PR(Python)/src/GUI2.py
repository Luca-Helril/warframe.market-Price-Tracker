import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping
from WarframeWiki import WarframeWiki
from tkinter import Tk, Label
from PIL import Image, ImageTk
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import Image
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import ttk



class MyGUI2:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Daten Sammlung")
        self.window.geometry("900x600")

        close_btn = ttk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack(pady=10)