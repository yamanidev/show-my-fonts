#pylint: disable=W0614

from tkinter import *
from tkinter.font import *


root = Tk()
root.title("Tkinter Fonts")
root.geometry("400x400")

fonts = list(families())
fonts.sort()

i = 0
current_font = fonts[i]
font_style = Font(family = current_font, size = 20)

def update():
    global i
    i += 1
    current_font = fonts[i]
    font_style = Font(family = current_font, size = 20)
    current_font_label.config(text = current_font)
    dummy_text.config(font = font_style)
    current_font_label.pack()
    dummy_text.pack()
    
current_font_label = Label(root, text = current_font)
dummy_text = Label(root, text = "I am a dummy text", font = font_style)
next = Button(root, text = "Next", width = 30, command = update)




current_font_label.pack(pady = 30)
dummy_text.pack()
next.pack(pady = 30)

root.resizable(0, 0)
root.mainloop()