import tkinter as tk
import sqlite3

class AddWindow:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.root = tk.Tk()
        self.root.geometry("260x260")
        self.root.config(background='#9da7d1')
       
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def window(self):
        window2Side = tk.Label(self.root, 
                                text="Website",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Side.place(y=20, relx = 0.5, anchor = tk.CENTER)

        window2Username = tk.Label(self.root, 
                                text="Username",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Username.place(y=80, relx = 0.5, anchor = tk.CENTER)

        window2Password = tk.Label(self.root, 
                                text="Password",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        window2Password.place(y=140, relx = 0.5, anchor = tk.CENTER)

        e1 = tk.Entry(self.root,
                            font=('Arial',15))
        e1.place(y=45, relx = 0.5, anchor = tk.CENTER)

        e2 = tk.Entry(self.root,
                            font=('Arial',15))
        e2.place(y=105, relx = 0.5, anchor = tk.CENTER)

        e3 = tk.Entry(self.root,
                            font=('Arial',15))
        e3.place(y=165, relx = 0.5, anchor = tk.CENTER)

        window2AddButton = tk.Button(self.root, 
                                    text="Add",
                                    height=3,
                                    width=20,
                                    command= lambda: AddWindow.add(self, e1.get(), e2.get(), e3.get()))
        window2AddButton.place(y=215, relx = 0.5, anchor = tk.CENTER)
    def add(self, side, login, passwords):
        self.add_account( side, login, passwords)
        self.root.destroy()
    
    def add_account(self, page, login, password):
        query = 'INSERT INTO admin (name, login, password) VALUES (?, ?, ?)'
        self.cursor.execute(query, (page, login, password))
        self.conn.commit()        
    
a = AddWindow()
a.window()
a.root.mainloop