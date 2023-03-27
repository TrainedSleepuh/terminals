from termcolor import colored

tkin = colored('''

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hier steht der Titel")
root.geometry("400x400")

#root.minsize(width=250, height=250)                    # Minimum size
#root.maxsize(width=600, height=600)                    # Max size
#root.resizeable(width=False, height=False)             # Now window cant resize

label1 = tk.Label(root, text="Hallo Welt", bg="green")
#label1.pack(side="top", fill="x")                      # fill="x" (fills the whole x axis) (same for fill="y" but y axis)
label1.pack(side="top")

label2 = tk.Label(root, text="Hallo Welt", bg="red")
#label2.pack(side="top", expand=True, fill="both")      # fill="both" (fills whole section) # expand=True (puts label in middle)
label2.pack(side="top")

img = Image.open("luv.png").resize((100,100))
foto = ImageTk.PhotoImage(img)

dif_label = ttk.Label(root, text="Das ist unser Logo", image=foto, compound="top")
dif_label.pack()
dif_label.configure(font=("Arial", 30))
for item in dif_label.keys():
    print(item, ": ", dif_label[item])

root.mainloop()

''', 'red')

print(tkin)