import random

def load_passwords(file_path):
    try:
        with open(file_path, "r") as file:
            # Read all lines from the file and strip whitespace
            passwords = [line.strip() for line in file.readlines()]
        return passwords
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except IOError:
        print(f"Error: Could not read the file at {file_path}.")
        return []

def generator(file_path):
    passwords = load_passwords(file_path)  #read in passwords
    
    if not passwords:
        raise ValueError("No passwords available in the file.")
    
    # Select a random password from the list
    return (f"Your generated password is: {random.choice(passwords)}")

file_path = "text_files/passwords.txt" 
random_password = generator(file_path)
print(f"Randomly selected password: {random_password}")
