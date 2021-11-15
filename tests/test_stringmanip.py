from toolboxpack.stringmanip import add_comma
from toolboxpack.stringmanip import belongs_to
from toolboxpack.stringmanip import count_repetition
from toolboxpack.stringmanip import is_a_question
from toolboxpack.stringmanip import replace
from toolboxpack.stringmanip import remove_surrounding_whitespaces
from toolboxpack.stringmanip import full_description_concatenation
from toolboxpack.stringmanip import full_description_formatting


def test_add_comma():
    assert add_comma("boris romain seb") == "boris, romain, seb"

def test_include_word():
        """This method should return True as 'hey jude' contains 'jude'"""
        assert belongs_to("hey jude", "jude") ==  True

def test_numbers_0_0_1_2_0_on_3():
        """This method should return 0 if a_substring doesn't occur in a_string"""
        assert count_repetition("00120", "3") == 0

def test_is_a_question():
        """This method should return True when a_string ends with a '?'"""
        assert is_a_question("How are you?") == True

def test_leading_whitespaces():
        """This method should work with leading whitespaces"""
        assert remove_surrounding_whitespaces("  hey yo") == "hey yo"

def test_casanova_to_cosonovo():
        """This method should correctly replace the letter(s) in the string"""
        assert replace("casanova", "a", "o") == "cosonovo"

def test_john_doe_33_concatenation():
        """This method should correctly return the full name and the age"""
        assert full_description_concatenation("John", "Doe", 33) == "John Doe is 33"

def test_john_doe_33_formatting():
        """This method should correctly return the full name and the age"""
        assert full_description_formatting("John", "Doe", 33) == "John Doe is 33"