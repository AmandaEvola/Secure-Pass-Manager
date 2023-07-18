import hashlib

def hash_password(password):
   """Hash the password using SHA-256."""
   return hashlib.sha256(password.encode()).hexdigest()

def save_passwords(filename, passwords):
    """Save the passwords to a file."""
    with open(filename, 'w') as file:
        for account, password in password.items(): # Change 'password' to 'passwords' here
            file.write(f"{account}:{password}\n")

def load_passwords(filename):
    """Load the passwords from a file."""
    passwords={}
    with open(filename, 'r') as file:
        for line in file:
            account, password = line.strip().split(':')
            passwords[account] = password
    return passwords

def main():
    filename = "passwords.txt"
    passwords = load_passwords(filename)
    
    print("Password Manager")
    print("----------------")

    while True:
        print("\n1. View Passwords")
        print("2. Add Password")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
           if passwords:
               print("\nStored Passwords:")
               for account, password in passwords.items():
                   print(f"{account}: {password}")
           else:
                print("\nNo passwords stored yet.")

        elif choice == "2":
             account = input("Enter the account name: ")
             password = input("Enter the password: ")
             hashed_password = hash_password(password)
             passwords[account] = hashed_password
             save_passwords(filename, passwords)
             print("Password saved succesfully!")

        elif choice == "3":
            print("Existing Password Manager.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()