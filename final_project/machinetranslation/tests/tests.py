import unittest
from translator import french_to_english, english_to_french

class TestE2f(unittest.TestCase):
    def test1(self):
        #test that hello returns bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #test that hello does not return hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        #test None returns empty string
        self.assertNotEqual(english_to_french('None'),'')
        #test empy string returns empty string
        self.assertNotEqual(english_to_french(0),0)

class TestF2E(unittest.TestCase):
    def test1(self):
        #test that bonjour returns hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #test that bonjour does not return bonjour
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        #test None returns empty string
        self.assertNotEqual(french_to_english('Non'),'')
        #test empty string returns empty string
        self.assertNotEqual(french_to_english(0),0)

unittest.main()