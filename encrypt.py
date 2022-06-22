from cryptography.fernet import Fernet
import sqlite3

class FirstEnc:
    def __init__ (self):
        self.key = b'-rJUgd9UQ4gsPHd4PDRdKLrtfJnX0jpCTZBdn5ooVmM=' 
    def fLogin(self, login, password):
        print(self.key)
        fernet = Fernet(self.key)
        loginData = []
        loginData.append(fernet.encrypt(login.encode()))
        loginData.append(fernet.encrypt(password.encode()))
        return loginData
    def fDec(self, data):
        fernet = Fernet(self.key)
        password = []
        login = []
        arrayOfAccounts = []
        for n in range(0, len(data)):
            login.append(fernet.decrypt(data[n][0]).decode())
            password.append(fernet.decrypt(data[n][1]).decode())
        arrayOfAccounts.append(login)
        arrayOfAccounts.append(password)
        return arrayOfAccounts

class Encrypted:
    def __init__(self):
        self.key = b'-rJUgd9UQ4gsPHd4PDRdKLrtfJnX0jpCTZBdn5ooVmM=' 
    def enc(self, page, login, password):
        fernet = Fernet(self.key)
        enc = []
        enc.append(fernet.encrypt(page.encode()))
        enc.append(fernet.encrypt(login.encode()))
        enc.append(fernet.encrypt(password.encode()))
        return enc
    


class Dencrypted:
    def __init__(self):
        self.key = b'-rJUgd9UQ4gsPHd4PDRdKLrtfJnX0jpCTZBdn5ooVmM='     
    def denc(self, page, login):
        fernet = Fernet(self.key)
        dec = []
        dec.append(fernet.decrypt(page).decode())
        dec.append(fernet.decrypt(login).decode())
        return dec

class EDPassword:
    
    def __init__(self):
        self.key = b'-rJUgd9UQ4gsPHd4PDRdKLrtfJnX0jpCTZBdn5ooVmM=' 
    def denc(self, password):
        fernet = Fernet(self.key)
        decpass = (fernet.decrypt(password).decode())
        return decpass
    def enc(self, password):
        fernet = Fernet(self.key)
        cpass = (fernet.encrypt(password.encode()))
        return cpass