import unittest
import re
from PasswordGenerator.password_generator import PasswordGenerator

passwordGenerator = PasswordGenerator()

class PasswordGeneratorTest(unittest.TestCase):
    def test_specialcharacter_number(self):
        number_result = False
        special_character_result = False
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        for character in passwordGenerator.get_Password():
            if character.isdigit():
                number_result = True
                break

        if(regex.search(passwordGenerator.get_Password)):
            special_character_result = True

        self.assertTrue(number_result)
        self.assertTrue(special_character_result)

    def test_number(self):
        number_result = False
        special_character_result = False
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        for character in passwordGenerator.get_Password():
            if character.isdigit():
                number_result = True
                break

        if(regex.search(passwordGenerator.get_Password)):
            special_character_result = True

        self.assertTrue(number_result)
        self.assertFalse(special_character_result)
        
    def test_specialcharacter(self):
        number_result = False
        special_character_result = False
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        for character in passwordGenerator.get_Password():
            if character.isdigit():
                number_result = True
                break

        if(regex.search(passwordGenerator.get_Password)):
            special_character_result = True

        self.assertFalse(number_result)
        self.assertTrue(special_character_result)
                