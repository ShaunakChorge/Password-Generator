import random
import string

class PasswordGenerator:
    def __init__(self, length):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation
    
    def generate_password(self):
        password = ''.join(random.choice(self.characters) for i in range(self.length))
        return password

class PasswordManager:
    def __init__(self, filename):
        self.filename = filename
    
    def save_password(self, name, password):
        with open(self.filename, 'a') as f:
            f.write(f"{name.ljust(20)} {password}\n")
    
    def get_passwords(self):
        with open(self.filename, 'r') as f:
            passwords = f.readlines()
        return passwords

if __name__ == '__main__':
    try:
        print("\n\n\n")
        print("===================================")
        print("|     PASSWORD GENERATOR          |")
        print("===================================")
        name = input("\nEnter your name: ")
        length = int(input("Enter the length of the password: "))
        
        pg = PasswordGenerator(length)
        password = pg.generate_password()
        print("\nGenerated password:", password)
        
        filename = 'passwords.txt'
        pm = PasswordManager(filename)
        pm.save_password(name, password)
        print("Password saved to file.")
        
        passwords = pm.get_passwords()
        print("\nList of saved passwords:")
        print("Name".ljust(20), "Password")
        print("-" * 30)
        for p in passwords:
            name, password = p.strip().split()
            print(name.ljust(20), password)
        
        print("\nThank you for using PASSWORD GENERATOR!")
        print("===================================")
        print("\n\n\n")
    except ValueError:
        print("\nInvalid input. Please enter a valid integer for the password length.")
    except Exception as e:
        print("\nAn error occurred:", e)
