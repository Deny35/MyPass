import sqlite3
import tkinter as tk

class Modify():
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.geometry("260x140")
        self.root.config(background='#9da7d1')
        print('init')

    
    def __del__ (self):
        self.cursor.close()
        self.conn.close()
        print('del')


    def window(self, what, name, user, id):
        self.what = what
        self.name = name
        self.user = user 
        self.id = id
        print('start')
        window2Side = tk.Label(self.root, 
                                text=self.what,
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Side.place(y=20, relx = 0.5, anchor = tk.CENTER)

        text = tk.StringVar()
        text.set(self.name)
        print('a')
        e1 = tk.Entry(self.root,
                            textvariable = text,
                            font=('Arial',15))
        e1.place(y=45, relx = 0.5, anchor = tk.CENTER)


        window2AddButton = tk.Button(self.root, 
                                    text="Add",
                                    height=3,
                                    width=20,
                                    command= lambda: self.mod(e1.get()))
        window2AddButton.place(y=95, relx = 0.5, anchor = tk.CENTER)
        
    def mod(self, changeName ):
        query = f"UPDATE {self.user} SET {self.what} = '{changeName}' WHERE id = '{self.id}'"
        self.cursor.execute(query)
        self.conn.commit()

