import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from Scraping import Scraping
from WarframeWiki import WarframeWiki


class Warframe_Collection:
    def __init__(self, root):

        self.window = tk.Toplevel(root)
        self.window.title("Daten Sammlung")
        self.window.geometry("900x600")

        close_btn = ttk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack(pady=5)

        wf = WarframeWiki()
        primes_List = wf.get_primes_list()
        owed_list = wf.get_owned_list()


        # MAIN FRAME
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True)


        # CANVAS + SCROLLBAR
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Für scrollen mit maus
        self.bind_mousewheel(self.canvas)

        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)


        # FRAME IM CANVAS
        self.second_frame = ttk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.second_frame,
            anchor="nw"
        )

        # Canvas resize -> Frame passt sich an
        self.canvas.bind("<Configure>", self.resize_canvas)
        self.second_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # GRID CONFIG
        for i in range(5):
            self.second_frame.grid_columnconfigure(i, weight=1)

        self.images = []
        self.buttons = []

        zeile = 0

        for kategori in primes_List:
            for name in primes_List[kategori]:

                picture_name = name.lower().replace(" prime", "") + ".png"
                picture_path = r"D:\__ SAVES __\__PR__\Pictures" + "\\" + picture_name

                if os.path.exists(picture_path):
                    image = Image.open(picture_path)
                    image = image.resize((64, 64))
                    photoimage = ImageTk.PhotoImage(image)
                    self.images.append(photoimage)

                    # WARFRAME BUTTON
                    tk.Button(self.second_frame, text=name, image=photoimage, compound=tk.LEFT).grid(row=zeile, column=0, sticky="nsew", padx=2,pady=2)

                    bauteil_list = ["blueprint", "chassis", "neuroptics", "system"]

                    for spalte, bauteil in enumerate(bauteil_list, start=1):
                        besitz = owed_list[kategori][name][bauteil]

                        btn = tk.Button(self.second_frame, text=bauteil)

                        if besitz:
                            btn.config(bg="gray50")

                        btn.grid(row=zeile, column=spalte, sticky="nsew", padx=2, pady=2)

                        btn.config(command=lambda k=kategori, n=name, b=bauteil, wf=wf, btn=btn: self.change_state(k, n, b, wf, btn))

                        self.buttons.append(btn)

                    zeile += 1


    def resize_canvas(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    def change_state(self, kategori, name, bauteil, warframeWiki, btn):
        owned = warframeWiki.get_owned_list()
        current = owned[kategori][name][bauteil]
        new_state = not current

        warframeWiki.set_owed(kategori, name, bauteil, new_state)

        if new_state:
            btn.config(bg="gray50")
        else:
            btn.config(bg=ttk.Style().lookup("TButton", "background"))
    
    def bind_mousewheel(self, widget):
        widget.bind("<Enter>", lambda e: widget.bind_all("<MouseWheel>", self._on_mousewheel))
        widget.bind("<Leave>", lambda e: widget.unbind_all("<MouseWheel>"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    root.tk.call("source", "Azure/azure.tcl")
    root.tk.call("set_theme", "dark")

    Warframe_Collection(root)
    root.mainloop()
