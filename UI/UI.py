from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText


class App:
    def __init__(self):
        self.root = Tk()
        title = 'Моя база данных'
        self.root.title(title)
        self.root.geometry('1200x720+100+0')
        self.root.minsize(800, 600)
        self.text = ScrolledText(self.root)

    def draw_menu(self):
        menu_bar = Menu(self.root)
        self.root.configure(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Файл', underline=0,
                             menu=file_menu)

        sub_file_menu = Menu(file_menu, tearoff=0)
        sub_file_menu.add_command(label='Excel',
                                  command=self.open_file)
        sub_file_menu.add_command(label='CSV',
                                  command=self.open_file)
        sub_file_menu.add_command(label='TXT',
                                  command=self.open_file)
        file_menu.add_cascade(label='Импортировать',
                              menu=sub_file_menu,
                              underline=0)

        file_menu.add_cascade(label='Сохранить',
                              command=self.save_file)

        file_menu.add_separator()

        file_menu.add_command(label='Выход',
                              command=self.on_exit)

    def open_file(self):
        file_name = fd.askopenfilename()
        if file_name:
            with open(file_name, 'r') as f:
                self.text.insert(END, f.read())

    def save_file(self):
        name = fd.asksaveasfilename()

    def on_exit(self):
        choice = mb.askyesno('Выход', 'Вы действительно хотите выйти?')
        if choice:
            self.root.quit()

    def draw_widgets(self):
        self.draw_menu()
        self.text.pack()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
