import hashlib
import json
import os
from cryptography.fernet import Fernet
import random
import string

#creating a Class to handle all account functions
class Account:
    usernam=""
    # This function handles authorization of a user trying to sign in
    def auth(self):
        Account.usernam=input("Enter your username: ")
        Passcheck=input("Enter your Master Password: ")
        if os.path.exists("Mastercred.json"):
            with open("Mastercred.json", "r") as file:
                 dataforauth = json.load(file)
        else:
             print("no accounts created")
        try:
             self.salt=dataforauth[Account.usernam+"salt"]
             self.saltedpass=self.salt+Passcheck
             self.hashed_passcheck=hashlib.sha256(self.saltedpass.encode('utf-8')).hexdigest()
             if Account.usernam in dataforauth and dataforauth[Account.usernam]==self.hashed_passcheck:
                  print("Authorization successful")
                  return True
             else:
                  print("not authorized")
                  return False
        except:
             print("not authorized")
             return False 
     # This function handles the adding of new credentials to the vault for the user    
    def addCredentials(self):
        
        self.website=input("Add Website: ")
        self.username=input("Add Username: ")
        self.password=input("Add Password: ")
        key = Fernet.generate_key()
        f = Fernet(key)
        
        self.encrypted_username=f.encrypt(self.username.encode('utf-8')).decode('utf-8')
        self.encrypted_hashed_password=f.encrypt(self.password.encode('utf-8')).decode('utf-8')
        credentials={"username":self.encrypted_username,"password":self.encrypted_hashed_password}

        if os.path.exists(Account.usernam+"cred.json"):
            with open(Account.usernam+"cred.json", "r") as file:
                    data = json.load(file)
        else:
            data = {}


        data[self.website] = credentials

        with open(Account.usernam+"cred.json", "w") as file:
            json.dump(data, file, indent=4)

            print("Credentials saved securely!")
        if os.path.exists(Account.usernam+"keys.json"):
            with open(Account.usernam+"keys.json", "r") as file:
                    keys = json.load(file)
        else:
            keys = {}


        keys[self.website] = key.decode('utf-8')

        with open(Account.usernam+"keys.json", "w") as file:
            json.dump(keys, file, indent=4)
     # This function prints the credentials for the asked website
    def ViewCred(self):
        self.which_website_cred=input("Which website's credential you want to view: ")
        if os.path.exists(Account.usernam+"cred.json"):
             with open(Account.usernam+"cred.json", "r") as file:
                  self.credforview = json.load(file)
        else:
             print("no accounts created")
        if os.path.exists(Account.usernam+"keys.json"):
            with open(Account.usernam+"keys.json", "r") as file:
                    datafordecrypt = json.load(file)
        keyfordecrypt=datafordecrypt[self.which_website_cred]
        t=Fernet(keyfordecrypt.encode("utf-8"))
        self.neededcred=self.credforview[self.which_website_cred]
        self.showusername=t.decrypt(self.neededcred["username"].encode("utf-8")).decode("utf-8")
        self.showpassword=t.decrypt(self.neededcred["password"].encode("utf-8")).decode("utf-8")
        print("Username: "+self.showusername)
        print("Password: "+self.showpassword)
     
if __name__ == "__main__":
     while True:
          Action1=input('Do you want sign up(Yes/No): ')
# This handles sign up of a new account adding all the neccesary files and setting up the account
          if Action1=="yes"or Action1=="Yes":
               username=input("Enter Username: ")
               MasterPassword=input("Enter Master Password: ")
               salt = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
               salted_password=salt+MasterPassword
               hashpassword=hashlib.sha256(salted_password.encode('utf-8')).hexdigest()
               credfilename=username+"creds"
               keyfilename=username+"keys"
               if os.path.exists("Mastercred.json"):
                    with open("Mastercred.json", "r") as file:
                         Users = json.load(file)
               else:
                    Users = {}


               Users[username] = hashpassword
               Users[username+"salt"]=salt
               with open("Mastercred.json", "w") as file:
                    json.dump(Users, file, indent=4)
               with open(username+"cred.json", "w") as file:
                    json.dump({}, file, indent=4)
               with open(username+"keys.json", "w") as file:
                    json.dump({}, file, indent=4)
     # Here we handle all the sign in functianality from authorization,adding or viewing credentials using the class accounts
          Action2=input("Do you want to sign in(Yes/No): ")
          if Action2=="yes" or Action2=="Yes":
               TempUser=Account()
               if TempUser.auth() is True:
                    addorview=input("Do you want to add new credentials or view stored credentials: ")
                    if addorview=="add"or addorview=="Add":
                         TempUser.addCredentials()
                    elif addorview=="view":
                         TempUser.ViewCred()
     

