import random
import string

class PasswordGenerator:
    password = ""
    password_size = 150
    special_characters_choice = False
    number_choice = False
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    def generate_password(self):
        if(self.number_choice and self.special_characters_choice):
            self.password = ''.join(random.choices(self.letters + self.numbers + self.symbols, k=self.password_size))
        elif(self.number_choice):
            self.password = ''.join(random.choices(self.letters + self.numbers, k=self.password_size))
        elif(self.special_characters_choice):
            self.password = ''.join(random.choices(self.letters + self.symbols, k=self.password_size))
        else:
            self.password = ''.join(random.choices(self.letters, k=self.password_size))
    
    def get_password(self):
        return self.password

    def set_special_characters(self, specialCharacters):
        self.special_characters_choice = specialCharacters

    def set_numbers(self, numbers):
        self.number_choice = numbers

    def set_password_size(self, password_size):
        self.password_size = password_size
