import sqlite3
from encrypt import FirstEnc

class Loginlogic:
    def __init__(self):
        self.conn = sqlite3.connect(".database.db")
        self.cursor = self.conn.cursor()
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def check_user(self, username, password):
        dec = FirstEnc()
        query = f'SELECT username, password FROM login'
        self.cursor.execute(query)
        data = (self.cursor.fetchall())
        dencryptedData = dec.fDec(data)
        print(dencryptedData)
        self.conn.commit()
        for n in range(0, len(data)):
            if dencryptedData[0][n] == username and dencryptedData[1][n] == password:
                return True
        return False

