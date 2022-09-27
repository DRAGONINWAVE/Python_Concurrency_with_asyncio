import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Hello World app')
window.geometry('200x200')


def say_hello():
    print(f'Hello World')


hello_button = ttk.Button(window, text='Hello World', command=say_hello)
hello_button.pack()

window.mainloop()
