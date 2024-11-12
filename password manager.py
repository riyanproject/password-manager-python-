from cryptography.fernet import fernet

def write_key():
    key=fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)


def load_key():
    return open("key.key","rb").read()
    key=file.read()
    file.close()
    return key

master_pwd=input("what is the master password:")

key=load_key()=master_pwd.encode()
fer=fernet(key)

    
        
def view():
    with open("passwords.twt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw=data.split("|")
            print("User:",user,"|Password:",str((fer.decrypt(passw.encode)+"\n")))

def add():
    name=input("account name:")
    pwd=input("password:")

    with open("passwords.twt","a") as f:
        f.write(name+"|"+str((fer.encrypt(pwd.encode)+"\n"))
while True:
    mode=input("would u like to add a new password or view existing one or press q to quit.(add/view/q)").lower()
    if mode=="q":

        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("invalid mode")
        continue