import unittest
from disease_detection import matching_codes

class TestStringMethods(unittest.TestCase):


    def test_1(self):
        result = matching_codes("Zungengrundkarzinom")
        self.assertEqual(result, 'C01')

    def test_2(self):
        result = matching_codes("Karzinom des Zungengrundes")
        self.assertEqual(result, 'C01')

    def test_3(self):
        result = matching_codes("Ovarialzyste")
        self.assertEqual(result, 'N83.2')

    def test_4(self):
        result = matching_codes("Zyste des Ovars")
        self.assertEqual(result, 'N83.2')

    def test_5(self):
        result = matching_codes("Irgendeine Diagnose")
        self.assertEqual(result, 'not found')

    def test_6(self):
        result = matching_codes("")
        self.assertEqual(result, 'not found')

    def test_7(self):
        result = matching_codes("a b c d ")
        self.assertEqual(result, 'not found')








if __name__ == '__main__':
    unittest.main()