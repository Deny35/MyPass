import sqlite3

class ReadData():
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
    
    def __del__ (self):
        self.cursor.close()
        self.conn.close()
        
    def readData(self, user):
        query = f'SELECT * FROM {user}'
        self.cursor.execute(query)
        return(self.cursor.fetchall())
 