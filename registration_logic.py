import sqlite3
from encrypt import FirstEnc
'''
def create_table():
    #query = "DROP TABLE IF EXISTS login"
    #cursor.execute(query)
    #conn.commit()

    query = 'CREATE TABLE login(username VARCHAR UNIQUE, password VARCHAR)'
    cursor.execute(query)
    conn.commit()
'''
class RegisterLogic:
    def __init__(self):
        self.conn = sqlite3.connect(".database.db")
        self.cursor = self.conn.cursor()
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def add_user(self,username, password):
        change = FirstEnc()
        encAccount= change.fLogin(username, password)
        query = 'SELECT * FROM login WHERE username = ?'
        self.cursor.execute(query, [encAccount[0]])
        result = self.cursor.fetchone()
        if result is not None:
            return result
        else:
            query = 'INSERT INTO login (username, password) VALUES (?, ?)'
            print(type(encAccount[0]))
            print(type(encAccount[1]))

            self.cursor.execute(query, (encAccount[0], encAccount[1]))
            self.conn.commit()
            query = 'CREATE TABLE ' + username + '(id INTEGER PRIMARY KEY,name VARCHAR, login VARCHAR, password VARCHAR)'
            self.cursor.execute(query)
            self.conn.commit()
            return result
            