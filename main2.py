import customtkinter as ctk
from tkinter import *

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")


class Main_window:
    def __init__(self, root):
        width=500
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.title('Конвертер')
        root.resizable(width=False, height=False)

        self.combobox1 = ctk.CTkComboBox(root, values = ['Цельсий', 'Кельвин', 'Фарингейт'])
        self.combobox1.place(x=130, y=150)

        self.combobox2 = ctk.CTkComboBox(root, values = ['Цельсий', 'Кельвин', 'Фарингейт'])
        self.combobox2.place(x=330, y=150)

        label1 = ctk.CTkLabel(root, text='Введите число: ')
        label1.place(x=25, y=30)
        label2 = ctk.CTkLabel(root, text='Перевести из')
        label2.place(x=25, y=150)
        label3 = ctk.CTkLabel(root, text='в')
        label3.place(x=300, y=150)
        label4 = ctk.CTkLabel(root, text='Результат:')
        label4.place(x=25, y=350)
        
        self.textbox1 = ctk.CTkTextbox(root, width=100, height=30)
        self.textbox1.place(x=140, y=30)

        self.label5 = ctk.CTkLabel(root, text='')
        self.label5.place(x=110, y=350)

        button = ctk.CTkButton(root, text='Перевести', command=self.conv)
        button.place(x=25, y=250)
    
    def conv(self):
        res = 0
        inp = int(self.textbox1.get('1.0', END))
        if self.combobox1.get() == 'Цельсий':
            res = inp
        elif self.combobox1.get() == 'Кельвин':
            res = inp - 273.15
        elif self.combobox1.get() == 'Фарингейт':
            res = (inp - 32) * (5/9)
        
        if self.combobox2.get() == 'Цельсий':
            res = res
        if self.combobox2.get() == 'Кельвин':
            res = res + 273.15
        elif self.combobox2.get() == 'Фарингейт':
            res = res * (5/9) + 32
        
        self.label5.configure(text = str(res))
        
        

        

if __name__ == "__main__":
    root = ctk.CTk()
    app = Main_window(root)
    root.mainloop()
