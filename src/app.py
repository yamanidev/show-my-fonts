from tkinter import *
from tkinter.font import *

root = Tk()
root.title("Tkinter Fonts")
root.geometry("400x400")

fonts = list(families())
fonts.sort()

i = 0
current_font = fonts[i]
font_style = Font(family=current_font, size=20)


def nxt_command():
    global i
    global font_number
    i += 1
    current_font = fonts[i]
    font_style = Font(family=current_font, size=20)
    current_font_label.config(text=current_font)
    dummy_text.config(font=font_style)
    font_number.config(text=str(i + 1) + " / " + str(len(fonts)))
    current_font_label.pack()
    dummy_text.pack()


def previous_command():
    global i
    global font_number
    i -= 1
    current_font = fonts[i]
    font_style = Font(family=current_font, size=20)
    current_font_label.config(text=current_font)
    previous.config(state=ACTIVE)
    dummy_text.config(font=font_style)
    font_number.config(text=str(i + 1) + " / " + str(len(fonts)))
    current_font_label.pack()
    dummy_text.pack()


font_number = Label(root, text=str(i + 1) + " / " + str(len(fonts)))
current_font_label = Label(root, text=current_font)
dummy_text = Label(root, text="I am a dummy text", font=font_style)
nxt = Button(root, text="Next", width=30, command=nxt_command)
previous = Button(root, text="Previous", width=30, command=previous_command)

current_font_label.pack(pady=30)
dummy_text.pack()
font_number.pack()
nxt.pack(pady=30)
previous.pack()

root.resizable(0, 0)
root.mainloop()
