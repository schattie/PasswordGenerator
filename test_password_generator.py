import unittest
import re
from password_generator import PasswordGenerator

class PasswordGeneratorTest(unittest.TestCase):
    passwordGenerator = PasswordGenerator()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    def test_specialcharacter_number(self):
        self.passwordGenerator.set_numbers(True)
        self.passwordGenerator.set_special_characters(True)
        self.passwordGenerator.generate_password()
        number_result = False
        special_character_result = False

        for character in self.passwordGenerator.get_password():
            if character.isdigit():
                number_result = True
                break

        if(self.regex.search(self.passwordGenerator.get_password())):
            special_character_result = True

        self.assertTrue(number_result)
        self.assertTrue(special_character_result)

    def test_number(self):
        self.passwordGenerator.set_numbers(True)
        self.passwordGenerator.set_special_characters(False)
        self.passwordGenerator.generate_password()
        number_result = False
        special_character_result = False

        for character in self.passwordGenerator.get_password():
            if character.isdigit():
                number_result = True
                break

        if(self.regex.search(self.passwordGenerator.get_password())):
            special_character_result = True

        self.assertTrue(number_result)
        self.assertFalse(special_character_result)
        
    def test_specialcharacter(self):
        self.passwordGenerator.set_numbers(False)
        self.passwordGenerator.set_special_characters(True)
        self.passwordGenerator.generate_password()
        number_result = False
        special_character_result = False

        for character in self.passwordGenerator.get_password():
            if character.isdigit():
                number_result = True
                break

        if(self.regex.search(self.passwordGenerator.get_password())):
            special_character_result = True

        self.assertFalse(number_result)
        self.assertTrue(special_character_result)
                