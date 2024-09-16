def insultor(password):
    with open("PasswordGeneRate/passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if password == line.strip():
                return "BAD PASSWORD"
        return "good"