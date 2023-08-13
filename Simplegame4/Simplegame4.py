from cryptography.fernet import Fernet
#Ask user for master password

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)   

def view():
    with open('Passwords.txt', 'r') as f:
        
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    username = input("Account Name: ")
    password = input("Account Password: ")
    
    with open('Passwords.txt', 'a') as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view an existing password?(add/view/'q' to quit): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Please choose either 'add' or 'view'!")
        continue
        
        

