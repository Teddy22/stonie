import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz_with_basic_valid_input(self):
        self.assertEqual(fizzbuzz(3), 'fizz')
        self.assertEqual(fizzbuzz(5), 'buzz')
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

    def test_fizzbuzz_with_non_numeric_input(self):
        msg = "fizzbuzz function should return 'None' for any non-numeric input."
        self.assertEqual(fizzbuzz('heloo'), None, msg)
        self.assertEqual(fizzbuzz(None), None, msg)
        self.assertEqual(fizzbuzz(fizzbuzz), None, msg)

    def test_fizzbuzz_with_non_integer_numeric_input(self):
        msg = "fizzbuzz function should return 'None' for any non-integer numeric input."
        self.assertEqual(fizzbuzz(3.0), None, msg)
        self.assertEqual(fizzbuzz(5.0), None, msg)
        self.assertEqual(fizzbuzz(15.0), None, msg)

        
if __name__ == '__main__':
    unittest.main()
