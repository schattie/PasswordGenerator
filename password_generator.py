import random
import string

class PasswordGenerator:
    password = ""
    passwordSize = 50
    specialCharacters = False
    numbers = False
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    def generate_password(self):
        if(self.numbers and self.specialCharacters):
            self.password = ''.join(random.choice(self.letters + self.numbers + self.symbols) for i in range(self.passwordSize))
        elif(self.numbers):
            self.password = ''.join(random.choice(self.letters + self.numbers) for i in range(self.passwordSize))
        elif(self.specialCharacters):
            self.password = ''.join(random.choice(self.letters + self.symbols) for i in range(self.passwordSize))
        else:
            self.password = ''.join(random.choice(self.letters) for i in range(self.passwordSize))
    def get_Password(self):
        return self.password
