import tkinter as tk
from tkinter import filedialog as fd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        icon = tk.PhotoImage(file='4711243-200.png')
        self.title('Моя база данных')
        self.iconphoto(False, icon)
        self.geometry('1200x720+100+0')
        self.minsize(800, 600)
        self['background'] = '#f2f6d0'


class Main_menu(tk.Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Файл', underline=0,
                             menu=file_menu)

        sub_file_menu = tk.Menu(file_menu, tearoff=0)
        sub_file_menu.add_command(label='Excel',
                                  command=open_file)
        sub_file_menu.add_command(label='CSV',
                                  command=open_file)
        sub_file_menu.add_command(label='TXT',
                                  command=open_file)

        file_menu.add_cascade(label='Импортировать',
                              menu=sub_file_menu,
                              underline=0)
        file_menu.add_cascade(label='Сохранить',
                              command=save_file)

        file_menu.add_separator()
        file_menu.add_command(label='Выход', command=self.onExit)

    def onExit(self):
        self.quit()


def open_file():
    name = fd.askopenfilename()
    print(name)


def save_file():
    name = fd.asksaveasfilename()
    print(name)


app = App()
menu = Main_menu()
app.mainloop()
