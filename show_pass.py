import sqlite3
import tkinter as tk
from encrypt import EDPassword

class Show():
    def __init__(self):
        self.conn = sqlite3.connect(".database.db")
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.geometry("260x140")
        self.root.config(background='#9da7d1')
    
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def window(self, user, id):
        self.user = user 
        self.id = id
        self.name = self.mod()

        window2Side = tk.Label(self.root, 
                                text='Password',
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Side.place(y=45, relx = 0.5, anchor = tk.CENTER)


        e1 = tk.Label(self.root,
                            text = self.name,
                            font=('Arial',15),
                            width = 20)
        e1.place(y=105, relx = 0.5, anchor = tk.CENTER)
        
    def mod(self):
        query = f"SELECT password FROM {self.user} WHERE id = '{self.id}'"
        self.cursor.execute(query)
        password = (self.cursor.fetchall()[0][0])
        dec = EDPassword()
        password = dec.denc(password)
        return password

'''
m = Modify()
m.window('admin1', 1)
m.root.mainloop()
'''