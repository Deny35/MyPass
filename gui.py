import tkinter as tk
from login_logic import Loginlogic
from registration_logic import RegisterLogic
from add import AddWindow
from tkinter import ttk
from read_data import ReadData
from modify_data import Modify

class Main:
    def globalVariable(self, username):
        global globalUser
        globalUser = username

    def switchToSignUp(self):
        self.frame2.pack_forget()
        self.f1()
        self.frame1.pack(fill="both", expand="true")

    def switchToSignIn(self):
        self.frame1.pack_forget()
        self.frame2.pack(fill="both", expand="true")

    def logIn(self, username, password):
        logic  = Loginlogic()
        Main.globalVariable(self, username)
        result = logic.check_user(username, password)
        if result is not None:
            try:
                self.frame1.pack_forget()
            except:
                pass
            self.frame2.pack_forget()
            self.f3()
            self.frame3.pack(fill="both", expand="true")
            self.root.geometry("720x265")
            # set minimum window size value
            self.root.minsize(720, 265)
    
            # set maximum window size value
            self.root.maxsize(720, 265)
        else:
            self.frame2LoginInf['text'] = "Password or login is incorrect!" 

    def signUp(self, username, password):
        logic = RegisterLogic()
        result = logic.add_user(username, password)
        if result is not None:
            self.frame1SignUpInf['text'] = "Such a user already exists!" 
        else:
            self.switchToSignIn()

    def changeInfPass(self):
        self.frame1SignUpInf['text'] = "Passwords must be the same!" 

    def addAccount(self):
        add = AddWindow()
        add.window()
        del add
        return True

    def readAData(self):
        try:
            read = ReadData()
            print(read.readData(globalUser))
            return read.readData(globalUser)
        except:
            pass
    
    def selectItem(self, event):
                curItem = self.tree.item(self.tree.focus())
                col = self.tree.identify_column(event.x)

                if col == '#1':
                    pass
                elif col == '#2':
                    id = curItem['values'][0]
                    what = 'name'
                    name = curItem['values'][1]
                elif col == '#3':
                    id = curItem['values'][0]
                    what = 'login'
                    name = curItem['values'][2]
                elif col == '#4':
                    id = curItem['values'][0]
                    what = 'password'
                    name = curItem['values'][3]
                
                m = Modify()
                m.window(what, name, globalUser, id)
                          

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("420x520")
        # set minimum window size value
        self.root.minsize(420, 520)
        
        # set maximum window size value
        self.root.maxsize(420, 520)
        self.root.title("MyPass")
        icon = tk.PhotoImage(file="logo.png")
        self.root.iconphoto(True, icon)
        self.root.config(background='#9da7d1')
    
    def f1(self):
        #frame1 (signUp)
        self.frame1 = tk.Frame(bg="#9da7d1")


        self.frame1LoginLable = tk.Label(self.frame1, 
                            text="Username",
                            font=('Arial',22,'bold'),
                            background='#9da7d1')
        self.frame1LoginLable.place(y=20, relx = 0.5, anchor = tk.CENTER)

        self.frame1LoginEntry = tk.Entry(self.frame1,
                            font=('Arial',15))
        self.frame1LoginEntry.place(y=70, relx = 0.5, anchor = tk.CENTER)

        self.frame1Password1Lable = tk.Label(self.frame1, 
                                text="Password",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        self.frame1Password1Lable.place(y=120, relx = 0.5, anchor = tk.CENTER)

        self.frame1Password1Entry = tk.Entry(self.frame1,
                            font=('Arial',15),
                            show="*")
        self.frame1Password1Entry.place(y=170, relx = 0.5, anchor = tk.CENTER)

        self.frame1Password2Lable = tk.Label(self.frame1, 
                                text="Password",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        self.frame1Password2Lable.place(y=220, relx = 0.5, anchor = tk.CENTER)

        self.frame1Password2Entry = tk.Entry(self.frame1,
                            font=('Arial',15),
                            show="*")
        self.frame1Password2Entry.place(y=270, relx = 0.5, anchor = tk.CENTER)

        self.frame1SignUpInf = tk.Label(self.frame1, 
                                text="",
                                fg='red',
                                font=('Arial',12),
                                background='#9da7d1')
        self.frame1SignUpInf.place(y=300, relx = 0.5, anchor = tk.CENTER)

        self.frame1SignUpButton = tk.Button(self.frame1, 
                                    text="Sign Up",
                                    height=3,
                                    width=15,
                                    command= lambda: (Main.signUp(self, self.frame1LoginEntry.get(), self.frame1Password1Entry.get()) 
                                    if self.frame1Password1Entry.get()==self.frame1Password2Entry.get() 
                                    else Main.changeInfPass()))
        self.frame1SignUpButton.place(y=350, relx = 0.5, anchor = tk.CENTER)

    def f2(self):
        #frame2 (signIn)
        self.frame2 = tk.Frame(bg="#9da7d1")
        self.frame2.pack(fill="both", expand="true")

        self.frame2LoginPhoto = tk.PhotoImage(file="logo_login.png")
        self.frame2LoginPhotoLable = tk.Label(self.frame2, 
                                    image=self.frame2LoginPhoto,
                                    height=100,
                                    width=420)
        self.frame2LoginPhotoLable.place(y=100, relx = 0.5, anchor = tk.CENTER)

        self.frame2LoginInf = tk.Label(self.frame2, 
                                text="",
                                fg='red',
                                font=('Arial',12),
                                background='#9da7d1')
        self.frame2LoginInf.place(y=170, relx = 0.5, anchor = tk.CENTER)

        self.frame2LoginLable = tk.Label(self.frame2, 
                                text="Username",
                                font=('Arial',22,'bold'),
                                background='#9da7d1')
        self.frame2LoginLable.place(y=220, relx = 0.5, anchor = tk.CENTER)

        self.frame2LoginEntry = tk.Entry(self.frame2,
                                font=('Arial',15))
        self.frame2LoginEntry.place(y=270, relx = 0.5, anchor = tk.CENTER)

        self.frame2PasswordLable = tk.Label(self.frame2, 
                                    text="Password",
                                    font=('Arial',22,'bold'),
                                    background='#9da7d1')
        self.frame2PasswordLable.place(y=320, relx = 0.5, anchor = tk.CENTER)

        self.frame2PasswordEntry = tk.Entry(self.frame2,
                                font=('Arial',15),
                                show="*")
        self.frame2PasswordEntry.place(y=370, relx = 0.5, anchor = tk.CENTER)

        self.frame2NewUserLabel = tk.Label(self.frame2, 
                                    text="New user?",
                                    font=('Arial',9),
                                    background='#9da7d1')
        self.frame2NewUserLabel.place(y=410, relx = 0.3, anchor = tk.CENTER)

        self.frame2SignUpButton = tk.Button(self.frame2, 
                                    text="Sign Up",
                                    height=3,
                                    width=15,
                                    command= lambda: Main.switchToSignUp(self))
        self.frame2SignUpButton.place(y=450, relx = 0.3, anchor = tk.CENTER)

        self.frame2SignInButton = tk.Button(self.frame2, 
                                    text="Sign In",
                                    height=3,
                                    width=15,
                                    command= lambda: Main.logIn(self, self.frame2LoginEntry.get(), self.frame2PasswordEntry.get()))
        self.frame2SignInButton.place(y=450, relx = (0.7), anchor = tk.CENTER)

        #self.root.mainloop()
        
    def f3(self):
        def loop():
            a = Main.addAccount(self)
            if a==True:
                print("a")
                tree()
        self.frame3 = tk.Frame(bg="#9da7d1")
        def tree():       
            self.tree = ttk.Treeview(self.frame3, columns= ('id', 'Name', 'Login', 'Password'), show='headings')
            self.tree.bind('<ButtonRelease-1>', self.selectItem)
           
            self.tree.heading('id', text='id')
            self.tree.heading('Name', text='Name')
            self.tree.heading('Login', text='Login')
            self.tree.heading('Password', text='Password')

            self.tree.column('id', width = 2)
            self.tree.column('Name', width = 206)
            self.tree.column('Login', width = 206)
            self.tree.column('Password', width = 300)
            contacts = []  
            global accounts 
            accounts = Main.readAData(self)
            
            try:
                for n in range(0, len(accounts)):
                    contacts.append((accounts[n][0], accounts[n][1], accounts[n][2], accounts[n][3]))

                for contact in contacts:
                    self.tree.insert('', tk.END, values=contact)
            except:
                pass


            self.tree.grid(row=0, column=0, sticky='nsew')

            scrollbar = ttk.Scrollbar(self.frame3, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscroll=scrollbar.set)
            scrollbar.grid(row=0, column=1, sticky='ns')



        tree()

        self.frame3Modify = tk.Button(self.frame3, 
                                    text="Modify",
                                    height=2,
                                    width=20)
        self.frame3Modify.place(y=225, relx = (0))
        self.frame3Add = tk.Button(self.frame3, 
                                    text="Add",
                                    height=2,
                                    width=20,
                                    command= lambda: (loop()))
        self.frame3Add.place(y=225, relx = (0.20))
        self.frame3Delete = tk.Button(self.frame3, 
                                    text="Delete",
                                    height=2,
                                    width=20)
        self.frame3Delete.place(y=225, relx = (0.40))
        self.frame3ViewPassword = tk.Button(self.frame3, 
                                    text="View password",
                                    height=2,
                                    width=20)
        self.frame3ViewPassword.place(y=225, relx = (0.60))
        self.frame3CopyPassword = tk.Button(self.frame3, 
                                    text="Copy password",
                                    height=2,
                                    width=20)
        self.frame3CopyPassword.place(y=225, relx = (0.80))



m = Main()
m.f2()
m.root.mainloop()
