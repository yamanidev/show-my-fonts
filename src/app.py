try:
    # Python 2
    import Tkinter as tk
    from Tkinter import font
    import ttk
except ImportError:
    # Python 3
    import tkinter as tk
    from tkinter import font
    from tkinter import ttk

FONTS = sorted(set(font.families()))

root = tk.Tk()

# Label for dummy text
dummy_text = tk.Label(root, text="I am a cool dummy text", font=(FONTS[0], 20))
dummy_text.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


# Callback function whenever combobox selection is changed
def change_font(event=None):
    new_font = font.Font(root=root, family=event.widget.get(), size=20)
    dummy_text.config(font=new_font)


# Combobox for the system's fonts
fonts_combobox = ttk.Combobox(root, values=FONTS, state="readonly", width=30, font="Helvetica 12")
fonts_combobox.current(0)
fonts_combobox.bind("<<ComboboxSelected>>", change_font)
fonts_combobox.place(relx=0.5, y=200, anchor=tk.CENTER)

root.title("Tkinter Fonts")
root.geometry("400x400")
root.resizable(False, False)
root.mainloop()
