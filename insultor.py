import random

def insultor(password):
    with open("PasswordGeneRate/text_files/passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if password == line.strip():
                with open("PasswordGeneRate/text_files/insults.txt", "r") as insults:
                    return random.choice(insults.readlines())                  
        return "good password"
    
#Open passwords.txt as file
#If password is in file, open insults.txt and grab a random insult