import sqlite3
import tkinter as tk
from encrypt import EDPassword

class Modify():
    def __init__(self):
        self.conn = sqlite3.connect(".database.db")
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.geometry("260x140")
        self.root.config(background='#9da7d1')
    
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def window(self, what, name, user, id):
        self.what = what
        self.name = name
        self.user = user 
        self.id = id
        window2Side = tk.Label(self.root, 
                                text=self.what,
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Side.place(y=20, relx = 0.5, anchor = tk.CENTER)

        text = tk.StringVar()
        text.set(str(self.name))
        e1 = tk.Entry(self.root,
                            textvariable = text,
                            font=('Arial',15))
        e1.place(y=55, relx = 0.5, anchor = tk.CENTER)


        window2AddButton = tk.Button(self.root, 
                                    text="Confir",
                                    height=3,
                                    width=20,
                                    command= lambda: self.mod(e1.get()))
        window2AddButton.place(y=105, relx = 0.5, anchor = tk.CENTER)
        
    def mod(self, changeName):
        print(self.what)
        print(self.user)
        print(self.id)


        enc = EDPassword()
        changeN = enc.enc(changeName)
        print(f"UPDATE {self.user} SET {self.what} = {changeN} WHERE id = {self.id}")
        query = f"UPDATE {self.user} SET {self.what} = {changeN} WHERE id = {self.id}"
        self.cursor.execute(query)
        self.conn.commit()
        print("zmiana")

'''
m = Modify()
m.window('login', "login", 'admin1', 1)
m.root.mainloop()
'''