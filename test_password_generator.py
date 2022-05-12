import unittest
import re
from password_generator import PasswordGenerator

class PasswordGeneratorTest(unittest.TestCase):
    password_generator = PasswordGenerator()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    def test_specialcharacter_number(self):
        self.password_generator.set_numbers(True)
        self.password_generator.set_special_characters(True)
        self.password_generator.generate_password()

        self.assertTrue(self.number_checker())
        self.assertTrue(self.special_character_checker())

    def test_number(self):
        self.password_generator.set_numbers(True)
        self.password_generator.set_special_characters(False)
        self.password_generator.generate_password()

        self.assertTrue(self.number_checker())
        self.assertFalse(self.special_character_checker())
        
    def test_specialcharacter(self):
        self.password_generator.set_numbers(False)
        self.password_generator.set_special_characters(True)
        self.password_generator.generate_password()

        self.assertFalse(self.number_checker())
        self.assertTrue(self.special_character_checker())

    def number_checker(self):
        number_result = False
        for character in self.password_generator.get_password():
            if character.isdigit():
                number_result = True
                break
        return number_result    

    def special_character_checker(self):
        special_character_result = False

        if(self.regex.search(self.password_generator.get_password())):
            special_character_result = True

        return special_character_result


                