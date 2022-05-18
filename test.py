import tkinter as tk
  
  
root = tk.Tk()
root.geometry("200x100")
  
text = tk.StringVar()
text.set("This is the default text")
textBox = tk.Entry(root,textvariable = text)
  
SignUpButton = tk.Button(root, 
                                    text="Sign Up",
                                    command= lambda:print(textBox.get()))
SignUpButton.place(x = 100)

textBox.pack()

root.mainloop()