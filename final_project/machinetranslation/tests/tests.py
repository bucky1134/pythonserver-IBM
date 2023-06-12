import unittest
from translator import englis_to_french, french_to_english

class TranslatorTesting(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(englis_to_french("hello"),"bonjour")

        self.assertNotEqual(englis_to_french("hello"),"bonjourrfr")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("bonjour"),"hello")
        
        self.assertNotEqual(french_to_english("bonjour"),"helloooo")