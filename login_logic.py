import sqlite3

class Loginlogic:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def check_user(self, username, password):
        query = 'SELECT * FROM login WHERE username = ? AND password = ?'
        self.cursor.execute(query, (username, password))
        print("Dane: ", username, password)
        result = self.cursor.fetchone()
        self.conn.commit()
        return result

'''
from login_logic import Loginlogic
logic  = Loginlogic()
 
answer = input("Login (Y/N): ")
if answer.lower() == "y":
    username = input("Username: ")
    password = input("Password: ")
    if logic.check_user(username, password):
        print("Username correct!")
        print("Password correct!")
        print("Logging in...")
    else:
        print("Something wrong")
'''
