import requests
from bs4 import BeautifulSoup
from WarframeWiki import WarframeWiki
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping

import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Scraping import Scraping
from WarframeWiki import WarframeWiki

from tkinter.ttk import *
import os
import glob


import tkinter as tk
from tkinter import ttk, LEFT
from PIL import Image, ImageTk
import os

from graphviz import Digraph

# Graph im Chen-Notation Stil
dot = Digraph("ERD", format="png")
dot.attr(rankdir="LR", size="8")

# Entities
dot.node("Person", "Person\n(PersonID, Name, Geburtsdatum)", shape="box")
dot.node("Spieler", "Spieler\n(Rückennummer, Vertrag?)", shape="box")
dot.node("Trainer", "Trainer\n(Lizenz)", shape="box")
dot.node("Haupttrainer", "Haupttrainer", shape="box")
dot.node("Assistenztrainer", "Assistenztrainer", shape="box")
dot.node("Mannschaft", "Mannschaft\n(MannschaftID, Name)", shape="box")
dot.node("Spiel", "Spiel\n(SpielID, Datum, Ort)", shape="box")

# Relationships
dot.node("nimmtTeil", "nimmt teil an\n(von, bis)", shape="diamond")
dot.node("bestehtAus", "besteht aus\n(genau 15)", shape="diamond")
dot.node("gespieltVon", "gespielt von\n(exakt 2)", shape="diamond")
dot.node("hatHT", "hat\n(genau 1)", shape="diamond")
dot.node("hatAT", "hat\n(0..n)", shape="diamond")

# Edges: Generalization
dot.edge("Person", "Spieler", label="is-a")
dot.edge("Person", "Trainer", label="is-a")
dot.edge("Trainer", "Haupttrainer", label="is-a")
dot.edge("Trainer", "Assistenztrainer", label="is-a")

# Edges: Relationships
dot.edge("Spieler", "nimmtTeil")
dot.edge("Spiel", "nimmtTeil")
dot.edge("Mannschaft", "bestehtAus")
dot.edge("Spieler", "bestehtAus")

dot.edge("Spiel", "gespieltVon")
dot.edge("Mannschaft", "gespieltVon")

dot.edge("Mannschaft", "hatHT")
dot.edge("Haupttrainer", "hatHT")

dot.edge("Mannschaft", "hatAT")
dot.edge("Assistenztrainer", "hatAT")

# Render to file
file_path = "/mnt/data/ERD_Spielsystem"
dot.render(file_path, format="png", cleanup=True)

file_path + ".png"
