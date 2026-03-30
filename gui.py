import os
from shutil import copyfile

import tkinter as tk
from tkinter import filedialog, messagebox

from patch import apply_patches

SUPPORTED_GAMES = [
    ("SHOGUN2", "Shogun II"),
    ("ROME2", "Rome II"),
    ("ATTILA", "Attila")
]

DEFAULT_GAME = "SHOGUN2"

game_var = None

def select_dll():
    filepath = filedialog.askopenfilename(initialdir=os.path.curdir)
    if not filepath:
        return

    try:
        copyfile(filepath, filepath + ".backup")
        success = apply_patches(filepath, game_var.get())
        if(success):
            messagebox.showinfo("Success", "Patch applied successfully!")
        else:
            messagebox.showwarning("Warning", "Patch wasn't successful, maybe you chose the wrong file?")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to apply the patch:\n{e}")

def app():
    global game_var

    root = tk.Tk()
    root.title("Total Save Patcher")

    root.geometry("400x300")

    game_var = tk.StringVar(value=DEFAULT_GAME)

    tk.Button(root, text="Select File", command=select_dll).pack(padx=20, pady=20)

    for game in SUPPORTED_GAMES:
        code_name = game[0]
        title_name = game[1]
        radio_button = tk.Radiobutton(root, text=title_name, variable=game_var, value=code_name)

        radio_button.pack()

    root.mainloop()
