import sqlite3

class Delete:
    def __init__(self):
        self.conn = sqlite3.connect(".database.db")
        self.cursor = self.conn.cursor()
    def __del__ (self):
        self.cursor.close()
        self.conn.close()

    def del_account(self, user, id):
        query = f"DELETE FROM {user} WHERE id = '{id}'"
        self.cursor.execute(query)
        self.conn.commit()
